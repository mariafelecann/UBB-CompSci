--indexing assigment
use Pastry

drop table if exists Tc
drop table if exists Tb
drop table if exists Ta
create table Ta (
    aid int primary key,
    a2 int unique NOT NULL,
	a3 int
);

create table Tb (
    bid int primary key,
    b2 int NOT NULL
);

create table Tc (
    cid int primary key,
    aid int,
    bid int
    foreign key (aid) references Ta(aid) on delete cascade,
    foreign key (bid) references Tb(bid) on delete cascade
);

insert into Ta values
(1,1,0),(2,2,0),(3,3,0),(4,4,0),(5,5,0),(6,6,0),(7,7,0),(8,8,0),(9,9,0),(10,10,0),(11,11,0),(12,12,0),(13,13,0),(14,14,0);

-- a.) Write queries on Ta 

--clustered index scan;
select *
from Ta
where aid between 1 and 14;

--clustered index seek;
select *
from Ta
where aid = 2;

--nonclustered index scan;
create nonclustered index ix_a2 on Ta(a2);
select *
from Ta
where a2 between 1 and 14;

--nonclustered index seek;
select *
from Ta
where a2 = 3;

--key lookup
select a3
from Ta
where a2 = 2


--b. Write a query on table Tb with a WHERE clause of the form WHERE b2 = value
--and analyze its execution plan. Create a nonclustered index that can speed up the query. Examine the execution plan again.

insert into Tb values
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)

select *   
from Tb
where b2 = 3;

create nonclustered index ix_b2 on Tb(b2);  
select *   
from Tb
where b2 = 3;

--c. Create a view that joins at least 2 tables. 
--Check whether existing indexes are helpful; if not, reassess existing indexes / examine the cardinality of the tables.
insert into Tc values (1,1,1), (2,1,2), (3,4,2);
use Pastry
drop view if exists MyView
go
create view MyView as
select Ta.aid, Tb.bid
from Ta
inner join Tc on Tc.aid = Ta.aid
inner join Tb on Tb.bid = Tc.bid;
go;


EXEC sp_helpindex 'Ta';

EXEC sp_helpindex 'Tb';

EXEC sp_helpindex 'Tc';

create nonclustered index ix_aid on Tc(aid);
create nonclustered index ix_bid on Tc(bid);

select*
from MyView;