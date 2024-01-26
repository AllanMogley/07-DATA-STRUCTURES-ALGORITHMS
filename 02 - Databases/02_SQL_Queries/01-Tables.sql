set schema 'flattables';
-- select * from "Data_In" limit 50

create table if not exists org as(
	select company_name as company,
	"Date" as date
	from "Data_In"
	);
	
create table if not exists Open as(
	select "Open" as open,
	"Date" as date
	from "Data_In"
);

create table if not exists High as(
	select "High" as high,
	"Date" as date
	from "Data_In"
);

create table if not exists Low as(
	select "Low" as low,
	"Date" as date
	from "Data_In"
);

create table if not exists Close as(
	select "Close" as close,
	"Date" as date
	from "Data_In"
);

create table if not exists Adj_Close as(
	select "Adj Close" as adj_close,
	"Date" as date
	from "Data_In"
);

create table if not exists Volume as(
	select "Volume" as volume,
	"Date" as date
	from "Data_In"
)


select * from "Data_In" limit 10

select company, volume, volume.date from "volume" left join "org"
on org.date = volume.date
order by org.date desc
limit 50


