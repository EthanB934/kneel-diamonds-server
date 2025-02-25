CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`)
);

INSERT INTO `Metals` VALUES (null, "Gold", 500);
INSERT INTO `Metals` VALUES (null, "Silver", 250);
INSERT INTO `Metals` VALUES (null, "Brass", 175);
INSERT INTO `Metals` VALUES (null, "Tungsten", 75);

INSERT INTO `Styles` VALUES (null, "Diamond", 500);
INSERT INTO `Styles` VALUES (null, "Sapphire", 450);
INSERT INTO `Styles` VALUES (null, "Emerald", 400);
INSERT INTO `Styles` VALUES (null, "Jade", 350);
INSERT INTO `Styles` VALUES (null, "Amethyst", 300);
INSERT INTO `Styles` VALUES (null, "Opal", 250);
INSERT INTO `Styles` VALUES (null, "Zirconium", 25);

INSERT INTO `Sizes` VALUES (null, "Size 10", 100);
INSERT INTO `Sizes` VALUES (null, "Size 9", 90);
INSERT INTO `Sizes` VALUES (null, "Size 8", 80);
INSERT INTO `Sizes` VALUES (null, "Size 7", 70);
INSERT INTO `Sizes` VALUES (null, "Size 6", 60);

INSERT INTO `Orders` VALUES (null, 1, 1, 1);
INSERT INTO `Orders` VALUES (null, 4, 7, 2);
INSERT INTO `Orders` VALUES (null, 3, 1, 4);
INSERT INTO `Orders` VALUES (null, 1, 5, 2);
INSERT INTO `Orders` VALUES (null, 2, 4, 5);
INSERT INTO `Orders` VALUES (null, 2, 4, 1);
INSERT INTO `Orders` VALUES (null, 4, 3, 2);
INSERT INTO `Orders` VALUES (null, 2, 3, 2);
INSERT INTO `Orders` VALUES (null, 3, 6, 3);
INSERT INTO `Orders` VALUES (null, 1, 2, 1);
INSERT INTO `Orders` VALUES (null, 1, 2, 5);