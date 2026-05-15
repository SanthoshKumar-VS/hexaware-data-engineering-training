create database retail_project;

use retail_project;


create table products
(
    product_id int primary key,
    product_name varchar(100),
    category varchar(50),
    price int,
    cost int
);


create table stores
(
    store_id int primary key,
    store_name varchar(100),
    city varchar(50)
);


create table sales
(
    sale_id int primary key,
    product_id int,
    store_id int,
    quantity int,
    sale_date date,

    foreign key(product_id) references products(product_id),
    foreign key(store_id) references stores(store_id)
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



update products
set price = 700
where product_id = 2;



delete from sales
where sale_id = 6;



delimiter //

create procedure store_sales(in sid int)

begin

select
s.store_name,
sum(p.price * sa.quantity) as total_sales

from sales sa

join products p
on sa.product_id = p.product_id

join stores s
on sa.store_id = s.store_id

where sa.store_id = sid

group by s.store_name;

end //

delimiter ;



call store_sales(101);