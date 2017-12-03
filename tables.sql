create table findout
(
id integer primary key
,userid integer
,facttype varchar(255)
,value real
,entry_date timestamp default current_timestamp
,latest_ind integer
);

create table goals
(
id integer primary key
,userid integer
,goal varchar(255)
,value real
,entry_date timestamp default current_timestamp
,latest_ind integer
);

create table dimension
(
id integer primary key
,dimension varchar(255)
,facttype  varchar(255)
);
