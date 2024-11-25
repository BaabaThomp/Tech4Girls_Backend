--Setting Up and Populating a Database--

CREATE  DATABASE IF NOT EXISTS Tech4Girls_DB;
SHOW DATABASES;

USE Tech4Girls_DB;

CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY AUTO INCREMENT,
    Username VARCHAR(50)),
    email VARCHAR(100),
    Created_at TIMESTAMP CURRENT_TIMESTAMP
);

INSERT INTO Tech4Girls_DB(id, username, email, created_at)
VALUES
      (1, 'ama', 'ama@example.com'),
      (2, 'Abena',  'abena@example.com'),
      (3, 'adjoa', 'adjoa@example.com');
