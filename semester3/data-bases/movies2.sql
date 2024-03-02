use Movie
go
drop procedure if exists AddActorProduction
go
create procedure AddActorProduction(@idA int, @idP int, @entry int)
as
	declare @nr int
	set @nr = 0
	select @nr = count(*)
	from ActorProductions
	where id_a = @idA and id_p = @idP
	if @nr = 0
	begin
		insert into ActorProductions values (@idA, @idP, @entry)
	end
	else
	begin
		update ActorProductions
		set entry_mom = @entry
		where id_a = @idA and id_p = @idP
	end
go

use Movie
go
drop view if exists ActorAllProductions
go
create view ActorAllProductions as
	select name, id_p
	from Actors a inner join ActorProductions p on (a.id = p.id_a)
	group by name, id_p
	having count(*) = (
		select count(*)
		from Productions
	)
go