CREATE DATABASE mine_db;
CREATE USER 'Ely'@'localhost' IDENTIFIED BY 'Mine_db_123';
GRANT ALL PRIVILEGES ON mine_db.* TO 'Ely'@'localhost';
FLUSH PRIVILEGES;
