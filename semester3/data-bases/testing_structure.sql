if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRuns]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRuns]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tests]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tests]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Views]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Views]

GO



CREATE TABLE [Tables] (

	[TableID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunTables] (

	[TestRunID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunViews] (

	[TestRunID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRuns] (

	[TestRunID] [int] IDENTITY (1, 1) NOT NULL ,

	[Description] [nvarchar] (2000) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,

	[StartAt] [datetime] NULL ,

	[EndAt] [datetime] NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestTables] (

	[TestID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[NoOfRows] [int] NOT NULL ,

	[Position] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestViews] (

	[TestID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Tests] (

	[TestID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Views] (

	[ViewID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



ALTER TABLE [Tables] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tables] PRIMARY KEY  CLUSTERED 

	(

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunTables] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunViews] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRuns] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRuns] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestTables] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestViews] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Tests] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tests] PRIMARY KEY  CLUSTERED 

	(

		[TestID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Views] WITH NOCHECK ADD 

	CONSTRAINT [PK_Views] PRIMARY KEY  CLUSTERED 

	(

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] ADD 

	CONSTRAINT [FK_TestRunTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunTables_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestRunViews] ADD 

	CONSTRAINT [FK_TestRunViews_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestTables] ADD 

	CONSTRAINT [FK_TestTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestTables_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestViews] ADD 

	CONSTRAINT [FK_TestViews_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	),

	CONSTRAINT [FK_TestViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	)

GO


--1 pk, 0 fk



---- VIEWS
drop view if exists SingleTableView;
drop view if exists MultiTableJoinView;
drop view if exists GroupByJoinView;
USE Pastry;
go
CREATE VIEW SingleTableView
AS
SELECT id, first_name, last_name
FROM dbo.Customers;
go;

USE Pastry;
go
CREATE VIEW MultiTableJoinView
AS
SELECT C.id, C.first_name, C.last_name, P.name
FROM dbo.Customers C
JOIN dbo.Products P ON C.order_name = P.name;
go;

USE Pastry;
go
CREATE VIEW GroupByJoinView
AS
SELECT P.id, COUNT(PP.promo_id) AS PromotionCount
FROM dbo.Products P
LEFT JOIN dbo.ProductsPromotions PP ON P.id = PP.product_id
GROUP BY P.id;
go;

insert into dbo.Views  values 
('SingleTableView'),
('MultitableJoinView'),
('GroupByJoinView');



use Pastry
drop procedure if exists InsertTest
go
create procedure InsertTest
as
begin
	DECLARE @StartTimeCustomers DATETIME;
	declare @EndTimeCustomers DATETIME;
	SET @StartTimeCustomers = GETDATE();
	insert into Pastry.dbo.Customers values ('canolli', 'ana', 'pop');
	select *
	from Pastry.dbo.Customers;
	SET @EndTimeCustomers = GETDATE();
	insert into TestRuns values ('Insert Test on Customers', @StartTimeCustomers, @EndTimeCustomers);
	insert into TestRunTables (TestRunID, TableID, StartAt, EndAt) values (1,1, @StartTimeCustomers, @EndTimeCustomers);
	insert into TestTables (TestID, TableID, NoOfRows, Position)values (1,1,1000,1);


	DECLARE @StartTimeProducts DATETIME;
	declare @EndTimeProducts DATETIME;
	SET @StartTimeProducts = GETDATE();
	insert into Pastry.dbo.Products values (2,1,'canolli', 'almond flour, cheese', 12);
	select *
	from Pastry.dbo.Products;
	SET @EndTimeProducts = GETDATE();
	insert into TestRuns values ('Insert Test on Products', @StartTimeProducts, @EndTimeProducts);
	insert into TestRunTables (TestRunID, TableID, StartAt, EndAt) values (2,2, @StartTimeProducts, @EndTimeProducts);
	insert into TestTables values (1,2,1000,2);

	DECLARE @StartTimeProductsPromotions DATETIME;
	declare @EndTimeProductsPromotions DATETIME;
	SET @StartTimeProductsPromotions = GETDATE();
	insert into Pastry.dbo.ProductsPromotions values (1,10);
	select *
	from Pastry.dbo.ProductsPromotions;
	SET @EndTimeProductsPromotions = GETDATE();
	insert into TestRuns values ('Insert Test on ProductsPromotions', @StartTimeProductsPromotions, @EndTimeProductsPromotions);
	insert into TestRunTables (TestRunID, TableID, StartAt, EndAt) values (3,3, @StartTimeProductsPromotions, @EndTimeProductsPromotions);
	insert into TestTables values (1,3,1000,3);

	DECLARE @StartTimeView1 DATETIME;
	declare @EndTimeView1 DATETIME;
	SET @StartTimeView1 = GETDATE();
	select *
	from Pastry.dbo.SingleTableView;
	SET @EndTimeView1 = GETDATE();
	insert into TestRuns values ('Select Test on Single View', @StartTimeView1, @EndTimeView1);
	insert into TestRunViews values (4,1,1000,4);
	insert into TestViews values(1,1);


	DECLARE @StartTimeView2 DATETIME;
	declare @EndTimeView2 DATETIME;
	SET @StartTimeView2 = GETDATE();
	select *
	from Pastry.dbo.MultiTableJoinView;
	SET @EndTimeView2 = GETDATE();
	insert into TestRuns values ('Select Test on Multi View', @StartTimeView2, @EndTimeView2);
	insert into TestRunViews values (5,2,1000,5);
	insert into TestViews values(1,2);

	DECLARE @StartTimeView3 DATETIME;
	declare @EndTimeView3 DATETIME;
	SET @StartTimeView3 = GETDATE();
	select *
	from Pastry.dbo.GroupByJoinView;
	SET @EndTimeView3 = GETDATE();
	insert into TestRuns values ('Select Test on Group By View', @StartTimeView3, @EndTimeView3);
	insert into TestRunViews values (6,3,1000,6);
	insert into TestViews values(1,3);
end

go;



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

insert into Promotions
values
('promotion 1', GETDATE(), GETDATE());

USE Pastry;
drop procedure if exists DeleteTest;
go
CREATE PROCEDURE DeleteTest
AS
BEGIN
    
    declare @StartTimeDeleteCustomers DATETIME;
    declare @EndTimeDeleteCustomers DATETIME;
    SET @StartTimeDeleteCustomers = GETDATE();

    DELETE FROM Pastry.dbo.Customers
    WHERE id = (SELECT TOP 1 id FROM Pastry.dbo.Customers ORDER BY id DESC);

    SELECT *
    FROM Pastry.dbo.Customers;

    SET @EndTimeDeleteCustomers = GETDATE();
    INSERT INTO TestRuns VALUES ('Delete Test on Customers', @StartTimeDeleteCustomers, @EndTimeDeleteCustomers);
    INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt) VALUES (7, 1, @StartTimeDeleteCustomers, @EndTimeDeleteCustomers);
    INSERT INTO TestTables VALUES (2, 1, 1000, 4);

    
    DECLARE @StartTimeDeleteProducts DATETIME;
    DECLARE @EndTimeDeleteProducts DATETIME;
    SET @StartTimeDeleteProducts = GETDATE();

    DELETE FROM Pastry.dbo.Products
    WHERE id = (SELECT TOP 1 id FROM Pastry.dbo.Products ORDER BY id DESC);

    SELECT *
    FROM Pastry.dbo.Products;

    SET @EndTimeDeleteProducts = GETDATE();
    INSERT INTO TestRuns VALUES ('Delete Test on Products', @StartTimeDeleteProducts, @EndTimeDeleteProducts);
    INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt) VALUES (8, 2, @StartTimeDeleteProducts, @EndTimeDeleteProducts);
    INSERT INTO TestTables VALUES (2, 2, 1000, 5);

    
    DECLARE @StartTimeDeleteProductsPromotions DATETIME;
    DECLARE @EndTimeDeleteProductsPromotions DATETIME;
    SET @StartTimeDeleteProductsPromotions = GETDATE();

    DELETE FROM Pastry.dbo.ProductsPromotions
    WHERE promo_id = (SELECT TOP 1 promo_id FROM Pastry.dbo.ProductsPromotions ORDER BY promo_id DESC);

    SELECT *
    FROM Pastry.dbo.ProductsPromotions;

    SET @EndTimeDeleteProductsPromotions = GETDATE();
    INSERT INTO TestRuns VALUES ('Delete Test on ProductsPromotions', @StartTimeDeleteProductsPromotions, @EndTimeDeleteProductsPromotions);
    INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt) VALUES (9, 3, @StartTimeDeleteProductsPromotions, @EndTimeDeleteProductsPromotions);
    INSERT INTO TestTables VALUES (2, 3, 1000, 6);
end
go;

--delete from Tests;
delete from Tables;
DBCC CHECKIDENT ('[Tables]', RESEED, 0);
DBCC CHECKIDENT ('[Tests]', RESEED, 0);


INSERT INTO Tables  VALUES ('Customers');

--1 pk, at least 1 fk

INSERT INTO Tables  VALUES ('Products');

--multi pk

INSERT INTO Tables  VALUES ('ProductsPromotions');

--insert into Tests values ('ÍnsertTest');
--insert into Tests values ('DeleteTest');

delete from TestRunTables;
delete from TestRunViews;
delete from TestViews;
delete from TestTables;
delete from Pastry.dbo.Customers;
delete from Pastry.dbo.ProductsPromotions;
exec InsertTest;
exec DeleteTest;
select * from TestRunTables;
select * from TestRuns;
select * from TestTables;

select * from TestRunViews;
select * from TestViews;

--select * from Tables;
--select * from Tests;