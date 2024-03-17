alter table ids add primary key (i);
alter table adj_close add primary key (id);
alter table close add primary key (id);
alter table high add primary key (id);
alter table low add primary key (id);
alter table open add primary key (id);
alter table orgs add primary key (id);
alter table volume add primary key (id);



alter table ids add foreign key (id) references adj_close (id);
alter table ids add foreign key (id) references close (id);
alter table ids add foreign key (id) references high (id);
alter table ids add foreign key (id) references low (id);
alter table ids add foreign key (id) references open (id);
alter table ids add foreign key (id) references orgs (id);
alter table ids add foreign key (id) references volume (id);



