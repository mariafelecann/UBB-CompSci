use Shoes
go
drop table if exists WomenShoes
drop table if exists ShoeShop
drop table if exists Shoes
drop table if exists ShoeModels
drop table if exists Women
drop table if exists Shops

create table Shops
(
	shop_id int not null,
	shop_name varchar(30),
	shop_city varchar(30),
	primary key(shop_id)
);

create table Women
(
	wid int not null,
	first_name varchar(30),
	nr_money int,
	primary key(wid)
);

create table ShoeModels
(
	model_id int not null,
	name_model varchar(30),
	season varchar(30),
	primary key(model_id)
);

create table Shoes
(
	shoe_id int not null,
	price int,
	model int,
	primary key(shoe_id),
	foreign key(model) references ShoeModels(model_id) on delete cascade
);

create table ShoeShop
(
    shoe_id int not null,
	shop_id int not null,
	nr_shoe_available int,
	primary key(shoe_id, shop_id),
	foreign key(shoe_id) references Shoes(shoe_id) on delete cascade,
	foreign key(shop_id) references Shops(shop_id) on delete cascade
);

create table WomenShoes
(
	woman_id int not null,
	shoe_id int not null,
	number_bought int, 
	spent_amount int,
	primary key(woman_id, shoe_id),
	foreign key(woman_id) references Women(wid) on delete cascade,
	foreign key(shoe_id) references Shoes(shoe_id) on delete cascade
);


