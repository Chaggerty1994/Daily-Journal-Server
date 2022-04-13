CREATE TABLE `Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    `date` TEXT NOT NULL
    FOREIGN KEY(`mood_id`) REFERENCES `Table`(`mood`(`id`))
);

CREATE TABLE `moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
    `label` TEXT NOT NULL
);