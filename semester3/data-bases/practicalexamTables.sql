use BankingTest
go
drop table if exists InvestingsClients
drop table if exists BankingSClient
drop table if exists ClientBank
drop table if exists InvestingServices
drop table if exists BankingServices
drop table if exists Banks
drop table if exists Clients
go
create table Clients
(
	name_c varchar(20) not null,
	id int not null unique,
	primary key(id)
);

create table Banks
(
	id int not null,
	primary key(id)
);
create table BankingServices
(
	id int not null,
	id_bank int not null,
	primary key(id),
	foreign key(id_bank) references Banks(id) on delete cascade
);
create table InvestingServices
(
	id int not null,
	id_bank int not null,
	primary key(id),
	foreign key(id_bank) references Banks(id) on delete cascade
);
create table ClientBank
(
	id_bank int not null,
	id_client int not null,
	name_client varchar(20) not null,
	primary key(id_bank, id_client),
	foreign key (id_client) references Clients(id) on delete cascade
);
create table BankingSClient
(
	id_bankserv int not null,
	id_client int not null,
	primary key(id_bankserv, id_client),
	foreign key(id_bankserv) references BankingServices(id) on delete cascade,
	foreign key(id_client) references Clients(id) on delete cascade
);

create table InvestingsClients
(
	id_serv int not null,
	name_client varchar(20) not null,
	id_client int not null,
	primary key(id_serv, id_client),
	foreign key(id_client) references Clients(id) on delete cascade,
	foreign key(id_serv) references InvestingServices(id) on delete cascade
);