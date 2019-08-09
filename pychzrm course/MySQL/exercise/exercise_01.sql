-- 创建数据库 江湖
create database 江湖 default charset utf8 collate utf8_general_ci;

-- 创建侠客表 id,姓名,门派,设置外键
create table 江湖(
id int primary key auto_increment,
姓名 varchar(88) not null,
门派id int,
constraint fk_门派_江湖
foreign key(门派id) references 门派(id),
功法id int,
constraint fk_功法_江湖
foreign key(功法id) references 功法(id),
武器id int,
constraint fk_武器_江湖
foreign key(武器id) references 武器库(id)
on delete cascade
on update cascade);

insert into 江湖(姓名,门派id,功法id,武器id)
values ("乔峰",1,1,1),("聂风",2,2,2),("狗杂种",3,3,3),("令狐冲",4,4,4);

-- 创建门派：id，门派
create table 门派(
id int primary key auto_increment,
门派 varchar(36)
);

insert into 门派(门派)
values (丐帮),
(风神堂),
(侠客岛),
(华山派);

-- 创建功法表：id，名称
create table 功法(
id int primary key auto_increment,
名称 varchar(88)
);

insert into 功法(名称)
values ("九阳神功"),
("九阴白骨爪"),
("九宫凌"),
("九轩绝");

-- 创建武器库：id,兵器，门派
create table 武器库(
id int primary key auto_increment,
兵器 varchar(88),
门派id int);

-- 武器库设置外键列：门派id,
alter table 武器库 add constraint fk_门派_武器库
foreign key (门派id)
references 门派(id);

-- 武器库添加数据
insert into 武器库(兵器,门派id)
values ("轩辕剑",2),
("天涯明月刀",3),
("如意金箍棒",1),
("方天画戟",1);

-- 内连接
-- 江湖中查找乔峰的武器功法
select j.姓名,w.兵器,g.名称 from 江湖 as j
inner join 武器库 as w on j.武器id = w.id
inner join 功法 as g on g.id = j.功法id
where j.姓名 = "乔峰";







