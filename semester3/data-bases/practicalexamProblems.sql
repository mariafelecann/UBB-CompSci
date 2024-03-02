use BankingTest
go
drop procedure if exists AddClientServices
go
create procedure AddClientServices(@idC int, @nameC varchar(20), @idB int)
as
	declare @nrBanking int
	declare @nrInvesting int
	set @nrBanking = 0
	set @nrInvesting = 0

	select @nrBanking = count(*)
	from BankingServices b
	where b.id_bank = @idB

	select @nrInvesting = count(*)
	from InvestingServices i
	where i.id_bank = @idB

	if @nrBanking != 0 
	begin
		declare @idBankingServices int
		set @idBankingServices = 0
		select @idBankingServices = id
		from BankingServices
		where id_bank = @idB
		insert into BankingSClient values (@idBankingServices, @idC)
	end
	else
	begin
		if @nrInvesting != 0
		begin
			declare @idInvServices int
			set @idInvServices = 0
			select @idInvServices = id
			from InvestingServices
			where id_bank = @idB
			insert into InvestingsClients values (@idInvServices, @nameC, @idC)
		end
	end

go

insert into Clients values ('ana',1);
insert into Banks values (1), (2);
insert into BankingServices values (1,1);
insert into InvestingServices values(1,2);

exec AddClientServices 1,'ana',1;
select * from BankingSClient;

use BankingTest
go
drop view if exists ClientsBothServices
go
create view ClientsBothServices 
as
	select i.id_client, i.name_client
	from InvestingsClients i
	group by i.id_client, i.name_client
	having 1 < (
		select count(i2.id_client)
		from BankingSClient b inner join InvestingsClients i2 on(b.id_client = i.id_client)
		where b.id_client = i.id_client and i2.id_client = i.id_client
	)
go

select *
from ClientsBothServices


use BankingTest
go
drop function if exists MultipleBanksClients
go
create function MultipleBanksClients()
returns table
as
return 
	select c.name_client as client_name, c.id_serv as investing_services, c.id_bankserv as bank_services
	from (
		select i.name_client, i.id_serv, b.id_bankserv
		from InvestingsClients i inner join BankingSClient b on (b.id_client = i.id_client)
	) as c

go

select *
from MultipleBanksClients()


--answers for 1: 1 2, 2a, 3d