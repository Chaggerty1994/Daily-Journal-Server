CREATE TABLE `Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    `date` TEXT NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `moods`(`id`)
);

CREATE TABLE `moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);

CREATE TABLE `tags` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL

);

CREATE TABLE `entrytag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id` INTEGER NOT NULL,
    `tag_id` INTEGER NOT NULL,
    FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `tags`(`id`)
);

INSERT INTO `moods` VALUES (null, "happy");
INSERT INTO `moods` VALUES (null, "sad");
INSERT INTO `moods` VALUES (null, "energetic");
INSERT INTO `moods` VALUES (null, "lethargic");
INSERT INTO `moods` VALUES (null, "confused");
INSERT INTO `moods` VALUES (null, "confident");
INSERT INTO `moods` VALUES (null, "worried");


INSERT INTO `Entries` VALUES (null, "SQL", "learning sql is hard", 1, "04-14-2022");
INSERT INTO `Entries` VALUES (null, "javascript", "making forms is fun", 1, "04-20-2022");
INSERT INTO `Entries` VALUES (null, "python", "coding is a lot of information", 1, "04-26-2022");


INSERT INTO `tags` VALUES (null, "hard");
INSERT INTO `tags` VALUES (null, "fun");
INSERT INTO `tags` VALUES (null, "new");
INSERT INTO `tags` VALUES (null, "confusing");
INSERT INTO `tags` VALUES (null, "annoying");
INSERT INTO `tags` VALUES (null, "exciting");

