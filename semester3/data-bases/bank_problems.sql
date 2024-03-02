use Bank
go
drop procedure if exists DeleteTransactions
go
create procedure DeleteTransactions (@id_card int)
as
	delete
	from Transactions
	where card_id = @id_card
go

exec DeleteTransactions 1

INSERT INTO Customers (cid, cname, birth) VALUES
(1, 'Customer1', '1990-01-01'),
(2, 'Customer2', '1985-05-15');

INSERT INTO Acounts (iban, balance, holder) VALUES
(1001, 5000, 1),
(1002, 7000, 2);

INSERT INTO Cards (number, cvv, ac_iban) VALUES
(1, 123, 1001),
(2, 456, 1002);

INSERT INTO Atms (aid, address_atm) VALUES
(101, '123 Main St'),
(102, '456 Oak St');

INSERT INTO Transactions (tid, id_atm, sum_money, card_id, timet) VALUES
(1, 101, 200, 1, '12:30:00'),
(2, 102, 150, 2, '14:45:00');
insert into Transactions values
(3, 102, 200, 1, '14:45:00')

INSERT INTO AtmCards (id_atm, id_card) VALUES
(101, 1),
(102, 2);


select * from Cards;
select * from Customers;
select * from Acounts;
select * from Atms;
select * from Transactions;
select * from AtmCards;

use Bank
go
drop view if exists AllAtmsCards
go
create view  AllAtmsCards as
select number
from Cards c inner join Transactions t on (c.number = t.card_id)
group by number
having count(distinct c.ac_iban) = (
	select count(*)
	from Atms
)
go
select *
from AllAtmsCards


use Bank
go
drop function if exists CardsSum
go
create function CardsSum()
returns table
as
	return
		select c.number, c.cvv
		from Cards c inner join Transactions t on (c.number = t.card_id)
		group by c.number, c.cvv
		having sum(sum_money) > 20

go

select *
from CardsSum()
