use Cake
go
insert into CakeTypes values(1, 'type1', 'very good');
insert into Cakes values ('bestcake','round', 10,100,1);
insert into Orders values (1, '2024-01-09');

use Cake
go
drop procedure if exists AddToOrder
go
create procedure AddToOrder (@P int, @orderID int, @caken varchar(20))
as
	declare @nr int;
	set @nr = 0
	select @nr = count(*)
	from OrderCakes o
	where o.oid = @orderID and o.cid = @caken
	if @nr = 0
	begin
		insert into OrderCakes values (@orderID, @caken, @P);
	end
	else
	begin
		update OrderCakes
		set quantity = @P
		where oid = @orderID and cid = @caken
	end
go

exec AddToOrder 2,1,'bestcake'
select * from OrderCakes

use Cake
go
drop function if exists ChefsAllCakes
go
create function ChefsAllCakes()
returns table
as
	return
		select c.name, s.cake_n
		from Chefs c inner join ChefSpecialization s on (c.id = s.chef_id)
		group by c.name, s.cake_n
		having count(cake_n) = (
			select count(*)
			from CakeTypes
		)
go

select *
from ChefsAllCakes()