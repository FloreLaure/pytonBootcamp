### exercice 1


CREATE DATABASE publics;

CREATE TABLE items(
 items_id SERIAL PRIMARY KEY,
 name VARCHAR (50) ,
 prix MONEY (50)
)


CREATE TABLE customers(
 customers_id SERIAL PRIMARY KEY,
 Prenom VARCHAR (40) ,
 Nom VARCHAR (30)
)
insert into items(items_id, name,prix) values('1','Small Desk','100'),('2','Large desk','300'),('3','Fan','80')

insert into customers(customers_id,Prenom, Nom) values('1','Greg','Jones'),('2','Sandra','Jones'),('3','Scott','Scott'),('4','Trevor','Green'),('5','Melanie','Johnson')


SELECT * FROM items ORDER BY prix ASC;


SELECT * FROM items where prix >= 80 ORDER BY prix DESC;

SELECT Nom,Prenom FROM customers ORDER BY Prenom ASC FETCH FIRST 3 ROWS ONLY;


SELECT Nom FROM customers ORDER BY Nom DESC;




### exercice 2

## 1
SELECT * FROM customer;
## 2
SELECT (first_name, last_name) as full_name FROM customer;
## 3
SELECT DISTINCT create_date FROM customer;
## 4
SELECT * FROM customer ORDER BY first_name DESC;
## 5
SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate ASC;
## 6
SELECT address,phone FROM address WHERE district='Texas';
## 7
SELECT * FROM film WHERE film_id IN (15,150) ;
## 8
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title='African Egg';
## 9
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title ILIKE 'Af%';
## 10
SELECT  film_id,title,description,film.length,rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;
## 11
SELECT  film_id,title,description,film.length,rental_rate FROM film  ORDER BY rental_rate ASC  OFFSET 10 FETCH FIRST 10 ROWS ONLY;
## 12
SELECT p.amount, p.payment_date FROM payment p INNER JOIN customer c ON p.customer_id=c.customer_id ORDER BY c.customer_id ASC;
## 13
SELECT f.film_id,f.title,f.description,f.length,f.rental_rate FROM film f WHERE f.film_id NOT IN (SELECT film_id FROM inventory);
## 14
SELECT o.country, i.city FROM country o INNER JOIN city i ON i.country_id=o.country_id;

