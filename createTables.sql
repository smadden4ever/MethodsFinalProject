CREATE DATABASE MTgroupProject;
create table items (
	itemid serial primary key,
	stock int,
	price int,
	title varchar(50)
);
create table users (
	username varchar(25) primary key,
	firstname varchar(30),
	lastname varchar(30),
	password varchar(50),
	shippingaddress varchar(100),
	shippingstate varchar(20),
	shippingzip int,
	ccnum int
);
create table cart (
	cartid serial primary key,
	itemid int not null references items(itemid),
	username varchar(25) not null references users(username),
	quantity int,
	orderid serial,
	ordered boolean
);