DROP DATABASE db_csystem;
CREATE DATABASE db_csystem;
USE db_csystem;

CREATE TABLE tbl_csystem(account_id INT NOT NULL PRIMARY KEY auto_increment, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL,
 email VARCHAR(255) NOT NULL, password VARCHAR(30) NOT NULL, category VARCHAR(30) NOT NULL);
 
 CREATE TABLE tbl_task(task_id INT NOT NULL PRIMARY KEY auto_increment, task_title VARCHAR(255) NOT NULL, task_description VARCHAR(255) NOT NULL, date DATETIME);