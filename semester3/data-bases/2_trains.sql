use [Train Schedules]
drop procedure if exists AddStation
go
create procedure AddStation( @Route int, @Station int, @Arrival time, @Departure time)
as
	declare @nr int;
	set @nr = 0;
	select @nr = count(*) from StationRoutes S where S.r_id = @Route and S.s_id = @Station;
	if(@nr <> 0) begin
		update StationRoutes
		set StationRoutes.arrival = @Arrival, departure = @Departure
		where s_id = @Station and r_id = @Route
	end
	else begin
		insert into StationRoutes values
		(@Route, @Station, @Arrival, @Departure);
	end;
go
exec AddStation  1,1,'17:00', '17:10'

insert into Stations values ( 'maresal constantin prezan');
insert into TrainTypes values ('1', 'un tren foarte bun');
insert into Trains values ( 'top', '1');

insert into TrainRoutes values ( 'ruta top', 1);

select *
from StationRoutes;

use [Train Schedules]
go
drop view if exists RoutesPassingAllStations
go
create view RoutesPassingAllStations as
select routeid, route_name
from TrainRoutes r inner join StationRoutes ss on r.routeid = ss.r_id
group by r.routeid, r.route_name
having count(*) = (select count(*) from Stations);
go
select *
from RoutesPassingAllStations

use [Train Schedules]
go
drop function if exists ListNames
go
create function ListNames (@R int)
returns table
as
	return 
		select station_name
		from Stations s inner join StationRoutes ss on s.stationid = ss.s_id
		group by station_name
		having count(station_name) > @R;
go

select *
from ListNames(0)