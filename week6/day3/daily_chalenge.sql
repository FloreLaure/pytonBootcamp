##Partie 1
## 1
CREATE TABLE customer (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(40) NOT NULL,
	last_name VARCHAR(30) NOT NULL
);

CREATE TABLE customer_profile (
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT FALSE,
	customer_id INTEGER NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES customer(id)
);

## 2
INSERT INTO customer (
	first_name,last_name
	) 
VALUES('John','Doe'),('Jerome','Lalu'),('Lea','Rive');
## 3
INSERT INTO customer_profile (
	isLoggedIn,customer_id
	) 
VALUES(
	FALSE,(
		SELECT id FROM customer WHERE first_name='Jerome')
	),
	(	
	TRUE,(
		SELECT id FROM customer WHERE first_name='John')
	);

## 4
SELECT first_name FROM customer  cu INNER JOIN customer_profile cp ON cu.id=cp.customer_id WHERE cp.isLoggedIn=TRUE;
SELECT first_name ,isLoggedIn FROM customer  cu LEFT OUTER JOIN customer_profile cp ON cu.id=cp.customer_id;
SELECT COUNT(first_name) FROM customer cu INNER JOIN customer_profile cp ON cu.id=cp.customer_id WHERE cp.isLoggedIn=FALSE;

## Partie 2 
## 1
CREATE TABLE Book (
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(70) NOT NULL,
	author VARCHAR(40) NOT NULL
);

## 2
INSERT INTO Book (
	title,author
	) 
VALUES ('Alice In Wonderland','Lewis Carroll'),('Harry Potter','J.K Rowling'),('To kill a mockingbird','Harper Lee');
## 3
CREATE TABLE Student (
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL UNIQUE,
	age INTEGER NOT NULL CHECK (age<=15)
);
## 3
INSERT INTO Student (
	name,age
	) 
VALUES('John',12),('Lera',11),('Patrick',10),('Bob', 14);
## 5
CREATE TABLE Library (
	book_fk_id INTEGER NOT NULL ,
	student_id INTEGER NOT NULL ,
	borrowed_date DATE,
	PRIMARY KEY(book_fk_id,student_id),
	FOREIGN KEY(book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(student_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);
## 6
INSERT INTO Library (
	book_fk_id,student_id,borrowed_date
	) 
VALUES(	
	(SELECT book_id FROM Book WHERE title='Alice In Wonderland'),
	(SELECT student_id FROM Student WHERE name='John'),'2022-02-15'),
	((SELECT book_id FROM Book WHERE title='To kill a mockingbird'),
	(SELECT student_id FROM Student WHERE name='Bob'),'2021-03-03'),
	((SELECT book_id FROM Book WHERE title='Alice In Wonderland'),
	(SELECT student_id FROM Student WHERE name='Lera'),'2021-05-23'),
	((SELECT book_id FROM Book WHERE title='Harry Potter'),
	(SELECT student_id FROM Student WHERE name='Bob'),'2021-08-12')
);

## 7
SELECT * FROM Library;
SELECT s.name, b.title FROM Student s INNER JOIN Library l ON s.student_id=l.student_id INNER JOIN Book b ON b.book_id=l.book_fk_id;
SELECT AVG(s.age) as Average FROM Student s INNER JOIN Library l ON s.student_id=l.student_id INNER JOIN Book b ON b.book_id=l.book_fk_id;
DELETE FROM Student WHERE name='John';


