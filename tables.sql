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

create table goal_types
(id integer primary key
,goal_name varchar(255)
,cat varchar(255)
,type  varchar(255)
,ntrans varchar(255)
);
