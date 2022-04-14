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