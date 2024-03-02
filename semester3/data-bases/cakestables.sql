use Cake
go
drop table if exists ChefSpecialization
drop table if exists Chefs
drop table if exists OrderCakes
drop table if exists Orders
drop table if exists Cakes
drop table if exists CakeTypes
create table CakeTypes
(
	id int not null,
	name_type varchar(20),
	descr varchar(20),
	primary key(id)
);

create table Cakes
(
	name_cake varchar(20),
	shape varchar(20),
	weight_cake int,
	price int,
	typeid int not null,
	primary key(name_cake),
	foreign key(typeid) references CakeTypes(id) on delete cascade
);

create table Orders
(
	oid int not null,
	date_order date,
	primary key(oid)
);

create table OrderCakes
(
	oid int not null,
	cid varchar(20) not null,
	quantity int,
	primary key(oid, cid),
	foreign key(oid) references Orders(oid) on delete cascade,
	foreign key(cid) references Cakes(name_cake) on delete cascade
);

create table Chefs
(
	id int not null,
	name varchar(20),
	gender varchar(20),
	birth varchar(20),
	primary key(id)
);

create table ChefSpecialization
(
	chef_id int not null,
	cake_n varchar(20) not null,
	primary key(chef_id, cake_n),
	foreign key(chef_id) references Chefs(id) on delete cascade,
	foreign key(cake_n) references Cakes(name_cake) on delete cascade
);