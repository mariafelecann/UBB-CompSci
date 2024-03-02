use Pastry
GO
drop table if exists EmployeeProductAssignment
drop table if exists OrderDetails
drop table if exists Orders
drop table if exists Reviews
drop table if exists Customers
drop table if exists ProductsPromotions
drop table if exists Promotions
drop table if exists Inventories
drop table if exists Products
drop table if exists Categories
drop table if exists Suppliers
drop table if exists Empoyees
drop table if exists VersionOfSchema

use Pastry
create table VersionOfSchema(
	VersionNumber int primary key
);



CREATE TABLE Empoyees(
	id int IDENTITY(1,1) NOT NULL,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL,
	salary varchar(100),
	PRIMARY KEY(id)
);

CREATE TABLE Suppliers(
	id int IDENTITY(1,1) NOT NULL,
	name varchar(30),
	email varchar(30),
	contact_info varchar(30),
	PRIMARY KEY(id)
);

CREATE TABLE Categories(
	id int IDENTITY(1,1) NOT NULL,
	name varchar(30),
	PRIMARY KEY(id)
);


CREATE TABLE Products(
	id int IDENTITY(1,1) NOT NULL,
	supplier_id int NOT NULL,
	category_id int NOT NULL,
	name varchar(30) NOT NULL,
	ingredients varchar(250) NOT NULL,
	price int,
	PRIMARY KEY(id),
	FOREIGN KEY(supplier_id)
		REFERENCES Suppliers(id)
		ON DELETE CASCADE,
	FOREIGN KEY(category_id)
		REFERENCES Categories(id)
		ON DELETE CASCADE
);

CREATE TABLE Inventories(
	id int IDENTITY(1,1) NOT NULL,
	product_id int NOT NULL,
	quantity_added int,
	quantiy_sold int,
	remaining_quantity int,
	PRIMARY KEY(id),
	FOREIGN KEY(product_id)
		REFERENCES Products(id)
		ON DELETE CASCADE
);

CREATE TABLE Promotions(
	id int IDENTITY(1,1) NOT NULL,
	name varchar(50),
	start_date datetime,
	end_date datetime,
	PRIMARY KEY(id)
);

CREATE TABLE ProductsPromotions(
	promo_id int NOT NULL,
	product_id int NOT NULL,
	PRIMARY KEY(promo_id, product_id),
	FOREIGN KEY(promo_id)
		REFERENCES Promotions(id)
		ON DELETE CASCADE,
	FOREIGN KEY(product_id)
		REFERENCES Products(id)
		ON DELETE CASCADE
);


CREATE TABLE Customers(
	id int IDENTITY(1,1) NOT NULL,
	order_name varchar(50),
	first_name varchar(50),
	last_name varchar(50),
	PRIMARY KEY(id)
);

CREATE TABLE Reviews(
	id int IDENTITY(1,1) NOT NULL,
	product_id int NOT NULL,
	customer_id int NOT NULL,
	reviewer_name varchar(100),
	content varchar(255),
	rating int,
	published_date datetime,
	PRIMARY KEY(id),
	FOREIGN KEY(product_id)
		REFERENCES Products(id)
		ON DELETE CASCADE,
	FOREIGN KEY(customer_id)
		REFERENCES Customers(id)
		ON DELETE CASCADE
);

CREATE TABLE Orders(
	id int IDENTITY(1,1) NOT NULL,
	name_of_order varchar(30) NOT NULL,
	price_of_order int NOT NULL,
	customer_id int NOT NULL,
	product_id int NOT NULL,
	order_date datetime,
	PRIMARY KEY(id),
	FOREIGN KEY(customer_id)
		REFERENCES Customers(id)
		ON DELETE CASCADE,
	FOREIGN KEY(product_id)
		REFERENCES Products(id)
		ON DELETE CASCADE
);

CREATE TABLE OrderDetails(
	id int IDENTITY(1,1) NOT NULL,
	order_id int NOT NULL,
	order_name varchar(30) NOT NULL,
	details varchar(30),
	PRIMARY KEY(id),
	FOREIGN KEY(order_id)
		REFERENCES Orders(id)
		ON DELETE CASCADE
);


CREATE TABLE EmployeeProductAssignment(
    employee_id int NOT NULL,
    product_id int NOT NULL,
    PRIMARY KEY (employee_id, product_id),
    FOREIGN KEY (employee_id)
        REFERENCES Empoyees(id)
        ON DELETE CASCADE,
    FOREIGN KEY (product_id)
        REFERENCES Products(id)
        ON DELETE CASCADE
);

