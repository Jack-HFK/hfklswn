-- 1.左外连接:左表:teacher,右表:course,关联条件:teacher.course_id=course.id
/*select * from
teacher left join course
on teacher.course_id = course.id*/


-- 2.左外连接:左表:course,右表:teacher,关联条件:teacher.course_id=course.id
/*select * from
course left join teacher
on teacher.course_id = course.id;*/

-- 3.右外链接,左表:course,右表:teacher,关联条件:teacher.course_id = course.id
/*select * from
course right join teacher
on teacher.course_id = course.id;*/

-- 4.完整外连接(有误)
/*select * from
course full join teacher
on full.id = teacher.course_id*/

-- 5.查看没有参加过考试的同学的信息
/*select * from
student left join score
on student.id = score.stu_id
where score.score is null;*/

-- 6.子查询-查询student表中比'李四'年龄大的学员的信息
/*select * from student
where age > (select age from student where name='李四');*/
-- 1.查询考过"齐天大圣"老师所教课程的学员的信息
-- 1.1 查询"齐天大圣"老师所教授的课程的ID
-- select course_id from teacher where name='齐天大圣';
-- 1.2 从score表中查询出course_id的值为 "1" 的stu_id的值
/*select stu_id from score where course_id=(
    select course_id from teacher where name='齐天大圣'
);*/
-- 1.3 从student表中查询出id在以上查询结果中出现过的学员的信息
select * from student where id in (
    select stu_id from score where course_id=(
        select course_id from teacher where name='齐天大圣'
    )
);
-- 2.查询在score表中有成绩的学员的信息
-- 3.查询"Python基础"课程并且分数在80分以上的学员的姓名和毕业院校
-- 4.查询和"张三"相同班级以及相同专业的同学的信息











