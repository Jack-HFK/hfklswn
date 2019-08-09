-- 左外链接：左表：teacher,右表：course,
-- 关联条件：teacher.course_id = course.id
select * from
teacher left join course
on teacher.course_id = course.id;

-- 左外链接：右表：teacher,左表：course,
-- 关联条件：teacher.course_id = course.id
-- 关联结果相当于内连接？：
select * from
course left join teacher
on teacher.course_id = course.id;

-- 测试
select cname from
course left join teacher
on teacher.course_id = course.id;
where teacher.id is null;


-- 右外链接：左表：teacher,右表：course,
-- 关联条件：teacher.course_id = course.id
select * from
teacher right join course
on teacher.course_id = course.id;

-- 完整外链接
select * from
teacher full join course
on teacher.course_id = course.id;

-- 没参加考试的学生信息
select * from
student left join Score
on student.id = Score.stu_id
where Score.score is null;

--  子查询
-- 查询student表中比郝建年龄大的学员的信息
select * from student
where age >(
select age from student
where name="好健");

-- 查询考过老健所教课程的学员信息
select * from student
where id in(select stu_id from Score
where course_id = (
select course_id from teacher
where name = "逆风"));
-- 查询在score表中有成绩的学员信息
select * from student
where id in(select stu_id from Score
where score is not null);

-- 查询考过python基础课程并且分数在80分以上的姓名和毕业学校
select name,school from student
where id in(select stu_id from Score
where score > 80 and course_id = (
select id from course
where cname = "Python基础")
);

-- 查询和郝建相同班级以及相同专业的同学信息
select * from student
where name != "好健" and
class_id = (select class_id from student
where name = "好健" and major_id = (
select major_id from student
where name = "好健");

-- 创建man表:id,name,age
create table man(id int primary key auto_increment,
name varchar(30) not null,
age int not null,unique(id));

insert into man(name,age)
values("杨过",25),("乔峰",35),("吕布",28);



--创建wife表，目的是实现与man 之间的关系
create table wife(id int primary key auto_increment,
name varchar(30) not null,
age int not null,
teacher_id int,
constraint fk_tacher_wife foreign key(teacher_id)
references man(id),
unique(teacher_id));

-- 插入数据测试
insert into wife(name,age,teacher_id)
values ("小龙女",30,1),("阿紫",34,2),("铃铛",24,3)s;

-- 创建 son表：id, man_id,wife_id,
-- man与wife多对多关系时之间的第三张关联表 son
create table son(id int primary key auto_increment,
man_id int not null,
constraint fk_man_son foreign key(man_id)
references man(id),
wife_id int not null,
constraint fk_wife_son foreign key(wife_id)
references wife(id));

-- 添加测试代码

insert into son(man_id,wife_id)
values(1,17),(2,18);

