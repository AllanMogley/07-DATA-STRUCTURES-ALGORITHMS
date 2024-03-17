alter table adj_close add primary key (id);
alter table adj_close add foreign key (id) references close (id);
alter table close add primary key (id);
alter table high add primary key (id);
alter table low add primary key (id);
alter table open add primary key (id);
alter table orgs add primary key (id);
alter table volume add primary key (id);






