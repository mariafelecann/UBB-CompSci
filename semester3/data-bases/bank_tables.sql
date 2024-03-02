use Bank
go
drop table if exists AtmCards
drop table if exists Transactions
drop table if exists Atms
drop table if exists Cards
drop table if exists Acounts
drop table if exists Customers
create table Customers
(
    cid int not null,
	cname varchar(50) not null,
	birth date,
	primary key(cid)
);

create table Acounts
(
	iban int not null,
	balance int,
	holder int not null,
	primary key(iban),
	foreign key(holder) references Customers(cid) on delete cascade
);


create table Cards
(
	number int not null,
	cvv int,
	ac_iban int not null,
	primary key(number),
	foreign key (ac_iban) references Acounts(iban) on delete cascade

);


create table Atms
(
	aid int not null,
	address_atm varchar(30),
	primary key(aid)
);

create table Transactions
(
	tid int not null,
	id_atm int not null,
	sum_money int,
	card_id int not null,
	timet time,
	primary key(tid),
	foreign key(id_atm) references Atms(aid) on delete cascade,
	foreign key (card_id) references Cards(number) on delete cascade
);

create table AtmCards
(
	id_atm int not null,
	id_card int not null,
	primary key(id_atm, id_card),
	foreign key(id_atm) references Atms(aid) on delete cascade,
	foreign key(id_card) references Cards(number) on delete cascade
);
