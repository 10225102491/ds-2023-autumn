create table user1(
id int not null primary key,
name VARCHAR(20),
sex VARCHAR(20),
age INT,
phone VARCHAR(20)
);
insert into user1 (id,name,sex,age,phone) values (1,'张1','man',11,'123456');
insert into user1 (id,name,sex,age,phone) values (2,'张3','man',22,'234567');
insert into user1 (id,name,sex,age,phone) values (3,'张2','woman',33,'345678');
insert into user1 (id,name,sex,age,phone) values (4,'李','woman',44,'456789');
select * from user1 where age>=20 and age <=40
delete from user1 where name like '张%' ;
select avg(age) from user1;
select * from user1 where age>=20 and age <=40 and name like '张%' order by age desc;
create table team (
id int primary key,
teamname VARCHAR(255)
);
create table score(
id int primary key,
teamid int,
userid int,
score int,
foreign key (teamid) references team(id),
foreign key (userid) references dbo.user1(id)
);
insert into team (id,teamname) values (1,'ECNU');
insert into team (id,teamname) values (2,'?');
INSERT INTO score (id,teamid,userid,score) values (1,1,1,10);
INSERT INTO score (id,teamid,userid,score) values (2,1,2,20);
INSERT INTO score (id,teamid,userid,score) values (3,1,3,30);
INSERT INTO score (id,teamid,userid,score) values (4,2,4,40);
select * from team a join score b on a.id = b.teamid join user1 c on b.userid = c.id where teamname = 'ECNU' and age < 20
select sum(score) from team a join score b on a.id = b.teamid join user1 c on b.userid = c.id where teamname = 'ECNU'