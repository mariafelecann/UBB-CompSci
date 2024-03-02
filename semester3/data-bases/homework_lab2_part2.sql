--a) 

select name as product_name
from Products
where price > 5 or supplier_id > 2
union
select contact_info as telephone
from Suppliers
where id > 2

select convert(varchar(30), order_date, 120) as order_date
from Orders
where customer_id > 1 OR product_id > 1
union all
select convert(varchar(30), first_name) as first_name
from Customers
where id > 1;

--b)

select category_id + 1
from Products
where id in (1,2,3)
intersect
select id
from Categories

select top 2 id
from Suppliers
where name in ('heavenly sweets suppliers', 'crust&crumb distributors')
intersect
select supplier_id
from Products

--c)

select order_name
from OrderDetails
where details not in ('to be ready')
except
select name_of_order
from Orders
where order_date in (GETDATE())


select id
from Categories
where name not in ('british pastries', 'danish pastries')
except
select category_id
from Products

--d)  
-- left join

select e.first_name as employee_name, 
       p.name as product_name,
       pr.name as promotion_name
FROM EmployeeProductAssignment epa
left join Empoyees e on epa.employee_id = e.id
left join Products p on epa.product_id = p.id
left join ProductsPromotions pp on p.id = pp.product_id
left join Promotions pr on pp.promo_id = pr.id;


-- inner join

select c.first_name + ' ' + c.last_name as name, o.name_of_order
from Customers c
inner join Orders o on c.id = o.customer_id

-- right join

select details, o.price_of_order
from OrderDetails od
right join Orders o on o.id = od.order_id

-- full join

select o.name_of_order as orders, c.first_name as client, p.name as product
from Orders o
full join Customers c on o.customer_id = c.id
full join Products p on p.id = o.product_id

--e)

select name
from Products
where category_id in(
	select id
	from Categories
	where name in ('french pastries', 'italian pastries', 'austrian pastries')
)

select distinct order_name
from OrderDetails
where order_id in 
(
	select id 
	from Orders
	where customer_id in
	(
		select id
		from Customers
		where first_name in ('ionica', 'georgiana', 'delia')
	)
)

-- f)

select distinct name
from Categories c
where exists(
	select id
	from Products
	where id = c.id
)

select distinct details
from OrderDetails o
where exists(
	select id
	from Orders
	where id = o.order_id and order_date not in (GETDATE())
)

-- g)

select o.name_of_order
from Orders o, 
	( select avg(price) as average from Products) as price
where o.price_of_order > price.average

select o.name_of_order, customer.name
from Orders o, 
	(select order_name, first_name + ' ' + last_name as name
	 from Customers) as customer
where o.name_of_order = customer.order_name

-- h)

select top 2 count(id) as number_of_orders, product_id
from Orders
group by product_id
order by count(id)

select sum(price) as sum_price, supplier_id as supplier
from Products
group by supplier_id
having sum(price) > 3

select count(id) as orders, product_id as product
from Orders
group by product_id
having product_id in
(
	select product_id
	from Products
	where price > 3
)

select avg(remaining_quantity) as remaining_q, min(remaining_quantity) as q
from Inventories
group by product_id
having product_id in
(
	select id
	from Products
	where supplier_id in (1,2,3)
)
order by product_id

-- i)

select quantity_added + 5
from Inventories i
where quantiy_sold = any
(
	select count(id)
	from Orders o
	where i.product_id = o.product_id
)

select name
from Products p
where price = any
(
	select price_of_order
	from Orders o
	where p.id = o.product_id
)

select name
from Products p
where supplier_id > all
(
	select id
	from Suppliers s
	where name = 'heavenly sweets suppliers'
)

select price, name 
from Products p
where price > all
(
	select remaining_quantity
	from Inventories i
	where i.product_id = p.id
)


-- rewriting the last 2 with other operators:


select p.price, p.name
from Products p
INNER JOIN Inventories i on p.id = i.product_id
group by p.price, p.name
having p.price > max(i.remaining_quantity);

select p.name
from Products p
where p.supplier_id > (
    select max(id)
    from Suppliers
    where name = 'heavenly sweets suppliers'
);

-- rewriting the first two with in:

select quantity_added
from Inventories i
where quantiy_sold in
(
	select count(id)
	from Orders o
	where i.product_id = o.product_id
)

select name
from Products p
where price in
(
	select price_of_order
	from Orders o
	where p.id = o.product_id
)