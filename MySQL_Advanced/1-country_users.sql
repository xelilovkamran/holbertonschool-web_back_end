-- SQL script that creates a table users
-- Table creation script
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM ('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
    PRIMARY KEY(id)
);
