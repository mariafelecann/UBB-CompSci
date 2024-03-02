drop procedure if exists modify_type
drop procedure if exists undo_modify_type
drop procedure if exists add_column
drop procedure if exists remove_column
drop procedure if exists add_default_constraint
drop procedure if exists remove_default_constraint
drop procedure if exists add_primary_key_constraint
drop procedure if exists remove_primary_key_constraint
drop procedure if exists add_candidate_key_constraint
drop procedure if exists remove_candidate_key_constraint
drop procedure if exists add_foreign_key
drop procedure if exists remove_foreign_key
drop procedure if exists add_table
drop procedure if exists drop_table
drop procedure if exists update_to_version
go


create procedure modify_type
as
begin
	alter table Employees
	alter column salary varchar(30);
	update VersionOfSchema
	set VersionNumber = 1;
end;
go

create procedure undo_modify_type
as
begin
	alter table Employees
	alter column salary int;
	update VersionOfSchema
	set VersionNumber = 0;
end;
go

create procedure add_column
as
begin
	alter table Customers
	add email varchar(30);
	update VersionOfSchema
	set VersionNumber = 1;
end;
go

create procedure remove_column
as
begin
	alter table Customers
	drop column email;
	update VersionOfSchema
	set VersionNumber = 0;
end;
go

create procedure add_default_constraint
as
begin 
	alter table Employees
	add constraint DF_salary_constraint
	default 5000 for salary;
	update VersionOfSchema
	set VersionNumber = 1;
end;
go

create procedure remove_default_constraint
as
begin
	alter table Employees
	drop constraint DF_salary_constraint;
	update VersionOfSchema
	set VersionNumber = 0;
end;
go

create procedure add_primary_key_constraint
as
begin
	alter table Customers
	add constraint PK_customer primary key(id, last_name);
	update VersionOfSchema
	set VersionNumber = 1;
end;
go

create procedure remove_primary_key_constraint
as
begin
	alter table Customers
	drop constraint PK_customer;
	update VersionOfSchema
	set VersionNumber = 0;
end;
go

create procedure add_candidate_key_constraint
as
begin
	alter table Suppliers
	add constraint CK_suppliers 
	unique(name);
	update VersionOfSchema
	set VersionNumber = 1;
end;
go

create procedure remove_candidate_key_constraint
as
begin
	alter table Suppliers
	drop constraint CK_suppliers;
	update VersionOfSchema
	set VersionNumber = 0;
end;
go

create procedure add_foreign_key
as
begin
	alter table OrderDetails
	add constraint FK_employee
	foreign key(employeeID)
	references Employees(id);
	update VersionOfSchema
	set VersionNumber = 1;
end;
go

create procedure remove_foreign_key
as
begin
	alter table OrderDetails
	drop constraint FK_employee;
	update VersionOfSchema
	set VersionNumber = 0;
end;
go

create procedure add_table
as
begin
	create table new_table(
	id int primary key
	);
	update VersionOfSchema
	set VersionNumber = 1;
end;
go

create procedure drop_table
as
begin
	drop table if exists new_table;
	update VersionOfSchema
	set VersionNumber = 0;
end;
go

create procedure update_to_version
	@given_version int
as
begin
	declare @current_version int;
    select @current_version = VersionNumber FROM VersionOfSchema;
	if @current_version != @given_version
	begin
		if @given_version = 1
		begin
			exec modify_type;
			exec add_column;
			exec add_default_constraint;
			exec add_primary_key_constraint;
			exec add_candidate_key_constraint;
			exec add_foreign_key;
			exec add_table;
		end;
		else
		begin
			exec undo_modify_type;
			exec remove_column;
			exec remove_default_constraint;
			exec remove_primary_key_constraint;
			exec remove_candidate_key_constraint;
			exec remove_foreign_key;
			exec drop_table;
		end;
	end;
end;
go

use Pastry

exec update_to_version 1;