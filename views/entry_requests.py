import sqlite3
import json
from models import Entry
from models.mood import Mood
from models import Entry_Tag


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./daily_journal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
            ON m.id = e.mood_id
        
        """)

        # Initialize an empty list to hold all animal representations
        entries = []
        
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        db_cursor.execute("""
        SELECT
            et.id,
            et.entry_id,
            et.tag_id,
            t.label tag_label
        FROM entrytag et
        JOIN tags t
            on et.tag_id = t.id
        """
        )

        entry_tags = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['mood_id'], row['date'])
            mood = Mood(row['id'], row['mood_label'])

            entry.mood = mood.__dict__


            tags = []
            for et_row in entry_tags:
                if et_row["entry_id"] == row["id"]:
                    tags.append(et_row["tag_id"])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    '''gets a single entry'''
    with sqlite3.connect("./daily_journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date
        FROM entries e
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['concept'], data['entry'],
                      data['mood_id'], data['date'])

        return json.dumps(entry.__dict__)


def delete_entry(id):
    with sqlite3.connect("./daily_journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entries
        WHERE id = ?
        """, (id, ))


def get_entry_by_search(entry):
    with sqlite3.connect("./daily_journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date
        FROM entries e
        WHERE e.entry LIKE ?
        """, (f"%{entry}%", ))

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['mood_id'], row['date'])
            entries.append(entry.__dict__)

    return json.dumps(entries)


def create_journal_entry(new_entry):
    with sqlite3.connect("./daily_journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entries
            (concept, entry, mood_id, date)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['concept'], new_entry['entry'], new_entry['moodId'],
              new_entry['date']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id

        #loop through the tags after adding new entry 
        # within loop execute SQL command to INSERT a row to entry tag table

        for tag in new_entry['tags']:

            db_cursor.execute("""
            INSERT INTO entrytag
                (entry_id, tag_id)
            VALUES
                (?,?);
            """, (id, tag)
            )

    return json.dumps(new_entry)


def update_entry(id, new_entry):
    '''update animal function'''
    with sqlite3.connect("./daily_journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entries
            SET
                concept = ?,
                entry = ?,
                mood_id = ?,
                date  = ?       
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'],
              new_entry['mood_id'], new_entry['date'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
