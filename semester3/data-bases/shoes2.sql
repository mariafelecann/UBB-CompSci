use Shoes
go
drop procedure if exists AddShoeToShop
go
create procedure AddShoeToShop(@ShoeId int, @ShopId int, @NumberOfShoes int)
as
	declare @nr int;
	set @nr = 0;
	select @nr = count(*)
	from Shoes
	where shoe_id = @ShoeId;
	IF @nr = 0
    BEGIN
        print 'this shoe does not exist';
    END
	else
	begin
		set @nr = 0;
		select @nr = count(*)
		from Shops
		where shop_id = @ShopId;
		IF @nr = 0
		begin
			print 'this shop does not exist'
		end
		else
		begin 
			insert into ShoeShop values (@ShoeId, @ShopId, @NumberOfShoes);
		end
	end

		
go
use Shoes
go
drop view if exists Women2Shoes
go
create view Women2Shoes as
select w.first_name, s.shoe_id
from Women w inner join WomenShoes s on (w.wid = s.woman_id)
where s.number_bought >= 2
group by w.first_name, s.shoe_id