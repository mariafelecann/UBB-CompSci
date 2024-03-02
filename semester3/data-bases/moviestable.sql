use Movie
go
drop table if exists ActorProductions
drop table if exists MoviesDirector
drop table if exists Productions
drop table if exists Movies
drop table if exists Directors
drop table if exists Companies
drop table if exists Actors
go
create table Actors
(
	id int not null,
	name varchar(20),
	ranking int,
	primary key(id)
);
create table Companies
(
	id int not null,
	name varchar(20),
	primary key(id)
);
create table Directors
(
	id int not null,
	name varchar(20),
	nr_awards int,
	primary key(id)
);
create table Movies
(
	id int not null,
	name varchar(20),
	date_m date,
	company_id int not null,
	primary key(id),
	foreign key(company_id) references Companies(id) on delete cascade,
);
create table Productions
(
	id int not null,
	title varchar(20),
	movie_id int not null,
	primary key(id),
	foreign key(movie_id) references Movies(id) on delete cascade
);

create table MoviesDirector
(
	id_d int not null,
	id_m int not null,
	primary key(id_d, id_m),
	foreign key(id_d) references Directors(id) on delete cascade,
	foreign key(id_m) references Movies(id) on delete cascade
);

create table ActorProductions
(
	id_a int not null,
	id_p int not null,
	entry_mom int,
	primary key(id_a, id_p),
	foreign key (id_a) references Actors(id) on delete cascade,
	foreign key(id_p) references Productions(id) on delete cascade
);