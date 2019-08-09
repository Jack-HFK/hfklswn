-- 单行注释: --空格 注释内容
/* 多行注销 */


-- 创建course表:id,cname,cdion
create table course(
id int primary key auto_increment,
cname varchar(30) not null,
cduration int not null
)

-- 向course表中插入测试数据
insert into course(cname,cduration)
values
("Python基础",20),("Python高级",15),
("WEB基础",9),("Python Web",15),
("爬虫",10),("数据分析&人工智能",20);

-- 创建teacher表:id,name,age,gender,hobby,course_id
-- course_id是外键,引用自course表的主键id
create table teacher(
id int primary key auto_increment,
name varchar(30) not null,
age int not null,
gender varchar(2) not null,
hobby varchar(50) not null,
course_id int,
constraint fk_course_teacher foreign key(course_id)
references course(id)
);
-- 向teacher表中插入测试数据
insert into teacher
values
(null,"九尊刊",28,"M","大保健",1),
(null,"乐菲",14,"F","吹风",2),
(null,"逆风",28,"M","喝酒",3);

-- 创建major:id m_name
create table major(
id int primary key auto_increment,
m_name varchar(30) not null
);

--向major表中插入数据
insert into major(m_name) values
("AID"),("UID"),("JSD"),("WEB");

-- 创建student表：id,name,gender,age,school,class_id,major_id
create table student(
id int primary key auto_increment,
name varchar(50) not null,
gender varchar(2) not null,
school varchar(100) not null,
class_id int not null,
major_id int not null
);

-- 更新student表，增加外键关系在major_id上，引用子major表的主键id
alter table student
add constraint fk_major_student
foreign key(major_id)
references major(id);

-- 向student中添加测试数据
alter table student add age int not null after gender;

-- 向student中添加测试数据
insert into student(name,gender,age,school,class_id,major_id)
values
("小健","M",25,"哈佛大学",1,1),
("老健","M",25,"麻省理工大学",2,2),
("好健","M",25,"牛津大学",3,3);

-- 创建Classinfo表:id,classname,stasus
create table Classinfo(
id int primary key auto_increment,
classname varchar(50) not null,
stasus int not null
);

-- 向Classinfo中添加测试数据
insert into Classinfo(classname,stasus) values
("1901",0),("1902",1),("1903",1),("1904",1);

-- 修改student表结构，增加外键在class_id上，引用子classinfo表的主键id
alter  table student
add constraint fk_classinfo_student
foreign key(class_id)
references Classinfo(id);


-- 创建Score表：id,stu_id,course_id,score
create table Score(
id int primary key auto_increment,
stu_id int not null,
course_id int not null,
score float(2) not null
);

-- 更新Score表，增加外键关系在sttu_id上，引用子student表的主键id
alter table Score
add constraint fk_stu_id
foreign key(stu_id)
references student(id);

-- 更新Score表，增加外键关系在course_id上，引用子course表的主键id
alter table Score
add constraint fk_course_id
foreign key(course_id)
references course(id);

-- 向Score表中中添加测试数据
insert into Score values(1,1,1,88.50);

-- 删除score表中的fk_stu_id外键
alter table Score drop foreign key fk_stu_id;

--为Score表中的stu_id增加外键，引用student主键的id,并设置级联操作
alter table Score
add constraint fk_student_score
foreign key(stu_id)
references student(id)
on delete cascade
on update cascade;