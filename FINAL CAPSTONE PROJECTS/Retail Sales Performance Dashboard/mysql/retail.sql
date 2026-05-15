create database retail_project;

use retail_project;

create table products (
    product_id int,
    product_name varchar(50),
    category varchar(50),
    price int,
    cost int
);

create table stores (
    store_id int,
    store_name varchar(50),
    city varchar(50)
);

create table sales (
    sale_id int,
    product_id int,
    store_id int,
    quantity int,
    sale_date date
);

insert into products values
(1,'Laptop','Electronics',50000,45000),
(2,'Mouse','Electronics',500,300),
(3,'Keyboard','Electronics',1000,700),
(4,'Shoes','Fashion',2000,1500),
(5,'Tshirt','Fashion',800,500);

insert into stores values
(101,'Reliance Store','Mumbai'),
(102,'Dmart','Pune'),
(103,'Big Bazaar','Delhi');

insert into sales values
(1,1,101,2,'2026-05-01'),
(2,2,101,5,'2026-05-01'),
(3,4,102,3,'2026-05-02'),
(4,3,102,4,'2026-05-02'),
(5,5,103,6,'2026-05-03'),
(6,1,103,1,'2026-05-03');

select * from products;
select * from stores;
select * from sales;