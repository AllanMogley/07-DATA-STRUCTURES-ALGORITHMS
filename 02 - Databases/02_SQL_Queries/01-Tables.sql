create table if not exists orgs as
(
	select id, company_name as company,
	"Date" as date
	from a_datain
);

	
create table if not exists open as
(
	select id, "Open" as open,
	"Date" as date
	from a_datain
);


create table if not exists high as
(
	select id, "High" as high,
	"Date" as date
	from a_datain
);


create table if not exists low as
(
	select id, "Low" as low,
	"Date" as date
	from a_datain
);


create table if not exists close as
(
	select id, "Close" as close,
	"Date" as date
	from a_datain
);


create table if not exists adj_close as
(
	select id, "Adj Close" as adj_close,
	"Date" as date
	from a_datain
);


create table if not exists volume as
(
	select id, "Volume" as volume,
	"Date" as date
	from a_datain
)



