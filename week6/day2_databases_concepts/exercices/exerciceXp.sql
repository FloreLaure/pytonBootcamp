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