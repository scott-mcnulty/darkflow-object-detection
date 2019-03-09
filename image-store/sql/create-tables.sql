CREATE TABLE IF NOT EXISTS `image_store_db`.`labels` (
    `record_id` INT AUTO_INCREMENT PRIMARY KEY,
    `label` VARCHAR(30) NOT NULL,
    `image_id` INT NOT NULL,
    `record_creation_time` DATETIME DEFAULT CURRENT_TIMESTAMP
) DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `image_store_db`.`locations` (
    `image_id` INT AUTO_INCREMENT PRIMARY KEY,
    `file_location_path` VARCHAR(250) NOT NULL,
    `record_creation_time` DATETIME DEFAULT CURRENT_TIMESTAMP
) DEFAULT CHARSET=utf8;