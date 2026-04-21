USE studentdb;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
);

INSERT INTO students (name, age, grade) VALUES
('Aman', 22, 'A')
('Somya', 22, 'F')
('Raj', 24, 'B' )