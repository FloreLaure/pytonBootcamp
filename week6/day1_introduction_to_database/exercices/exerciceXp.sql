
## exercice1

CREATE DATABASE publics;

CREATE TABLE items(
 items_id SERIAL PRIMARY KEY,
 name VARCHAR (50) ,
 prix MONEY (50) ,
)


CREATE TABLE customers(
 customers_id SERIAL PRIMARY KEY,
 Prenom VARCHAR (40) ,
 Nom VARCHAR (30) ,
)

insert into items(items_id, name,prix) values('1','Small Desk','100'),('2','Large desk','300'),('3','Fan','80')

insert into customers(customers_id,Prenom, Nom) values('1','Greg','Jones'),('2','Sandra','Jones'),('3','Scott','Scott'),('4','Trevor','Green'),('5','Melanie','Johnson')


##  3    

######  1
select * from items;


#####  2
select * from items where prix > 80;

###### 3
select * from items where prix <= 300;

###### 4
select * from customers where Nom = "Smith" ;


###### 5
select * from customers where Nom = "Jones" ;


###### 6
select * from customers where Prenom != "Scott" ;

