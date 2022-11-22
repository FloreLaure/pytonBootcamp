## 1
CREATE TABLE items(
   id SERIAL NOT NULL,
   nom VARCHAR(30) NOT NULL,
   price NUMERIC NOT NULL,
   PRIMARY KEY(id)
);

## 2

 CREATE TABLE product_orders(
   id SERIAL NOT NULL,
   id_items INTEGER NOT NULL,
   num VARCHAR(20) NOT NULL UNIQUE,
   date_com date NOT NULL,
   PRIMARY KEY(id),
   CONSTRAINT fk_items FOREIGN KEY (id_items) REFERENCES items(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE users(
    id SERIAL NOT NULL,
    product_orders_id INTEGER NOT NULL,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_product_orders FOREIGN KEY (product_orders_id) REFERENCES product_orders(id) ON DELETE CASCADE ON UPDATE CASCADE
 );

## 3 

CREATE OR REPLACE FUNCTION prix_total(fn VARCHAR(50)) 
 RETURNS NUMERIC AS $prixtotal$
 BEGIN
    RETURN(SELECT SUM(items.price) FROM items INNER JOIN product_orders ON items.id = product_orders.id_items WHERE product_orders.num = fn);
 END;
 $prixtotal$ LANGUAGE plpgsql;



## 4
CREATE OR REPLACE FUNCTION prix_total1(fn VARCHAR(50), lan VARCHAR(50)) 
 RETURNS NUMERIC AS $prixtotal$
 BEGIN
    RETURN(SELECT SUM(items.price) FROM items INNER JOIN product_orders ON items.id = product_orders.id_items WHERE product_orders.num = fn AND product_orders.num = lan);
 END;
 $prixtotal$ LANGUAGE plpgsql;

