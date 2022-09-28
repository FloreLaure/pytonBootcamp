

CREATE DATABASE bootcamp;

CREATE TABLE students(
 student_id SERIAL PRIMARY KEY,
 last_name VARCHAR (30) ,
 first_name VARCHAR (40) ,
 birth_date date() 

)


insert into students(student_id, first_name,last_name, birth_date) values('1','Marc','Benichou' '02/11/1998'),
('2','Yoan',' Cohen ' '03/12/2010'),('3','Lea','Benichou'; '27/07/1987'),('4','Amelia','Dux', '07/04/1996'),('5','David','Grez','14/06/2003'),('6','Omer','Simpson', '03/10/1980'),

### select
####1

select * from students;

####2
select first_name,last_name from students;

### 3 . a
select first_name,last_name from students where student_id=2;


###  3.  b
select first_name,last_name from students where last_name="Benichou" AND first_name="Marc";


###  3.  d
select first_name,last_name from students where first_name="a%";



###  3.  e
select first_name,last_name from students where first_name="%a";

