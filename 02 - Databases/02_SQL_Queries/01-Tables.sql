create table if not exists orgs as
(
	select id, company_name as company,
	"Date" as date
	from a_datain
);

	
create table if not exists open as
(
	select id, open,
	"Date" as date
	from a_datain
);


create table if not exists high as
(
	select id, high,
	"Date" as date
	from a_datain
);


create table if not exists low as
(
	select id, low,
	"Date" as date
	from a_datain
);


create table if not exists close as
(
	select id, close,
	"Date" as date
	from a_datain
);


create table if not exists adj_close as
(
	select id, adjclose,
	"Date" as date
	from a_datain
);


create table if not exists volume as
(
	select id, volume,
	"Date" as date
	from a_datain
)



