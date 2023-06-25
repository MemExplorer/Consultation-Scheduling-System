/* Actual MySQL code for database implementation, for use testing use cases. */

DROP DATABASE IF EXISTS db_csystem;
CREATE DATABASE db_csystem;
USE db_csystem;

-- Table for accounts, account_id = 100.
CREATE TABLE tbl_accounts (
    account_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(60) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role CHAR(1)
);

CREATE TABLE tbl_faculty(
history_id INT NOT NULL PRIMARY KEY auto_increment,
teacher_id INT REFERENCES tbl_accounts(account_id),
schedule_name VARCHAR(30) NOT NULL, 
scheduled_on DATE NOT NULL,
open_at TIME NOT NULL,
close_at TIME NOT NULL,
status ENUM("Open", "Reserved", "Ended")
);

CREATE TABLE tbl_consultations(
history_id INT NOT NULL PRIMARY KEY auto_increment, 
task_name VARCHAR(60) NOT NULL, 
task_description VARCHAR(60) NOT NULL,
created_by INT REFERENCES tbl_accounts(account_id),
requested_to INT REFERENCES tbl_accounts(account_id),
created_on DATETIME, 
status ENUM("Accepted", "Rejected", "Pending", "Ended") NOT NULL, 
ended_on DATETIME);

ALTER TABLE tbl_accounts AUTO_INCREMENT = 100000;
ALTER TABLE tbl_faculty AUTO_INCREMENT = 200000;
ALTER TABLE tbl_consultations AUTO_INCREMENT = 300000;

-- Test values for tbl_accounts
INSERT INTO tbl_accounts (first_name, last_name, username, email, password, role)
VALUES ('John', 'Doe', 'John Doe', 'johndoe@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'S'),
       ('Teacher', 'Doe', 'Teacher Doe', 'teacherdoe@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Nortz', 'Alingod', 'Nortz Alingod', 'nortzalingod@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T'),
       ('Jackie', 'Murallon', 'Jackie Murallon', 'jackiemurallon@gmail.com', 'Z0FBQUFBQmtpOGFPWE1jel8xcHJJWlMzRXptZFE4dThLVjhyNmJ3NDdjMjVTbDhhVHV1eFpyTWlkc3A0NVN3VkdPSkVKRkRQZmk1VkJkRUFIdUlBclIwRW9wR2lFYVhyTWc9PQ==', 'T');

-- Test values for tbl_faculty
INSERT INTO tbl_faculty (teacher_id, schedule_name, scheduled_on, open_at, close_at, status)
VALUES (100002, "Schedule 1 Open", '2023-06-28', '10:00:00', '12:00:00', "Open"), (100003, "Schedule 1 Open", '2023-06-27', '12:00:00', '14:00:00', "Open"), (100002, "Schedule 2 Closed",'2023-06-29', '13:00:00', '16:00:00', "Reserved"), (100003, "Schedule 2 Closed", '2023-06-29', '9:00:00', '11:30:00', "Reserved");

-- Test values for tbl_consultations
INSERT INTO tbl_consultations (task_name, task_description, created_by, requested_to, created_on, status, ended_on)
VALUES
    ('Task 1', 'Description 1', 100000, 100001, '2023-06-12 10:00:00', 'Accepted', '2023-06-13 15:30:00'),
    ('Task 2', 'Description 2', 100000, 100002, '2023-06-13 14:00:00', 'Rejected', NULL),
    ('Task 3', 'Description 3', 100000, 100002, '2023-06-13 14:00:00', 'Pending', NULL),
    ('Task 4', 'Description 3', 100000, 100003, '2023-06-14 12:30:00', 'Ended', '2023-06-15 09:45:00');