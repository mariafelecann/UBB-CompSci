use [Train Schedules]
go
drop table if exists Trains
drop table if exists TrainTypes
drop table if exists Stations
drop table if exists TrainRoutes
drop table if exists StationRoutes
use [Train Schedules]

create table TrainTypes(
typename varchar(30) not null,
typedescription varchar(200) not null
primary key(typename)
);

create table Trains(
tid int identity(1,1) not null,
tname varchar(30) not null,
train_type varchar(30) not null,
primary key(tid),
foreign key(train_type) REFERENCES TrainTypes(typename) on delete cascade);

create table Stations(
stationid int identity(1,1) not null,
station_name varchar(30) unique not null,
primary key(stationid)
);

create table TrainRoutes
(
routeid int identity(1,1) not null,
route_name varchar(30) not null,
train_id int not null,
primary key(routeid),
foreign key(train_id) references Trains(tid)
);

create table StationRoutes
(
s_id int not null,
r_id int not null,
arrival time,
departure time,
primary key(s_id, r_id),
foreign key(s_id) references Stations(stationid) on delete cascade,
foreign key(r_id) references TrainRoutes(routeid) on delete cascade
);

