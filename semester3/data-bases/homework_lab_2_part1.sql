use Pastry
alter table Products add unique(name);
--insert into OrderDetails
--values
--(999, 'strudel order', 'picked up');
insert into Empoyees
values
('adrian', 'popescu', 3500),
('elena', 'pop', 5000);

insert into Categories
values
('french pastries'),
('italian pastries'),
('austrian pastries'),
('danish pastries'),
('british pastries'),
('to be deleted');

insert into Suppliers
values
('heavenly sweets suppliers','heaven@sweets.com', '0757645897'),
('crust&crumb distributors', 'çrumb_distributor@gmail.com', '0733284294'),
('puff pastry provisions', 'provisions@pastry.com', '0756382956');

insert into Customers
values
('macarons order','delia', 'gherasim'),
('macarons order','georgiana', 'telecan'),
('strudel order','ionica', 'gabor'),
('cannoli order','dania', 'nedelcu');


insert into Products
values
(2, 2, 'cannoli', 'cannoli shells , ricotta cheese, powdered sugar, chopped nuts', 12),
(1,3,'strudel', 'pastry sheets, apples, sugar and cinnamon mixture', 10),
(3,1, 'macarons', 'almond flour, sugar, egg whites', 20);

insert into Orders
values
('strudel order',10,1,2, GETDATE()),
('macarons order',20,1,3, GETDATE()),
('macarons order',30,2,3, GETDATE()),
('cannoli order',22, 3,2, GETDATE());


insert into OrderDetails
values
(1, 'strudel order', 'picked up'),
(2, 'macarons order', 'to be ready'),
(3, 'macarons order', 'picked up'),
(4, 'cannoli order', 'picked up)'); 

insert into Inventories
values
(1,15,4,11),
(2,17,10,7),
(3,6,6,0);

insert into EmployeeProductAssignment
values
(1,1),
(1,2),
(2,2),
(1,3);

update Products
set price = 9
where category_id = 3 and name is not null

update Customers
set last_name = 'felecan'
where id > 1 and first_name = 'georgiana'

update Suppliers
set contact_info = '0711111111'
where id = 1 and name like 'h%';

delete from Categories
where id = 6

delete from Customers
where last_name in ('deleted', 'telecan')

delete from Products
where id > 4 and price between 5 and 15

delete from Products;
delete from Orders;
delete from OrderDetails;
delete from Customers;
delete from Categories;
delete from EmployeeProductAssignment;
delete from Empoyees;
delete from Suppliers;
delete from Inventories;
