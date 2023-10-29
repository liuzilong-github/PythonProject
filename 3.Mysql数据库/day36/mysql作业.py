#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/3/21 15:20
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : mysql作业.py
@Software: PyCharm

'''
# 1、查询所有的课程的名称以及对应的任课老师姓名
"""
select
	c.cname, t.tname
from
	course as c
	inner join teacher as t on c.teacher_id = t.tid;
"""

# 2、查询学生表中男女生各有多少人
"""
select
	gender, count(*)
from
	student
group by
	gender;
"""

# 3、查询物理成绩等于100的学生的姓名
"""
select
	sd.sname
from
	student as sd 
	inner join score as sc on sd.sid = sc.student_id
	inner join course as c on sc.course_id = c.cid
where
	c.cname = "物理" and sc.num = 100;
"""

# 4、查询平均成绩大于八十分的同学的姓名和平均成绩
"""
select
	sd.sname, avg(sc.num)
from
	score as sc
	inner join student as sd on sd.sid = sc.student_id
group by
	sc.student_id
having
	avg(sc.num) > 80;
"""

# 5、查询所有学生的学号，姓名，选课数，总成绩
"""
select
	sd.sid, sd.sname, count(*), sum(sc.num)
from
	score as sc
	inner join student as sd on sd.sid = sc.student_id
group by
	sc.student_id;
"""

# 6、 查询姓李老师的个数
"""
select
	count(*)
from
	teacher
where
	tname like "李%";
"""

# 7、 查询没有报李平老师课的学生姓名
"""
select
	sd.sid,
	sd.sname 
from
	student AS sd 
where
	sd.sid not in (
	select
		distinct(sc.student_id) 
	from
		score AS sc
		INNER JOIN course AS c ON sc.course_id = c.cid
		INNER JOIN teacher AS t ON c.teacher_id = t.tid 
	where
		tname = "李平" 
	);
"""

# 8、 查询物理课程的分数比生物课程的分数高的学生的学号
"""
select
	t1.student_id
from
	(select
	s.student_id, s.num
from
	course as c
	inner join score as s on c.cid = s.course_id
where
	c.cname = "物理") as t1 inner join (select
	s.student_id, s.num
from
	course as c
	inner join score as s on c.cid = s.course_id
where
	c.cname = "生物") as t2 on t1.student_id = t2.student_id
where
	t1.num > t2.num
group by
	t1.student_id;

"""

# 9、 查询没有同时选修物理课程和体育课程的学生姓名
"""
select
	sid, sname 
from
	student 
where
	sid not in (
	select
		student_id 
	from
		score 
	where
		course_id in (
		select
			cid 
		from
			course 
		where
			cname = "物理" 
			or cname = "体育" 
		) 
	group by
		student_id 
	having
		count( * ) = 2 
	);
"""

# 10、查询挂科超过两门(包括两门)的学生姓名和班级
"""
select
	sd.sname, c.caption
from
	student as sd 
	inner join score as sc on sd.sid = sc.student_id
	inner join class as c on c.cid = sd.class_id
where
	sc.num < 60
group by
	sc.student_id
having
	count(*) >= 2;
"""

# 11、查询选修了所有课程的学生姓名
"""
select
	sd.sname 
from
	score as sc
	inner join student as sd on sc.student_id = sd.sid 
group by
	sc.student_id 
having
	count(*) = ( select count(*) from course );
"""

# 12、查询李平老师教的课程的所有成绩记录
"""
select
	sc.num
from
	score as sc
	inner join course as c on sc.course_id = c.cid
	inner join teacher as t on c.teacher_id = t.tid
where
	t.tname = "李平";
"""

# 13、查询全部学生都选修了的课程号和课程名
"""
select
	c.cid, c.cname 
from
	score as s
	inner join course as c on s.course_id = c.cid 
group by
	course_id 
having
	count(*) = (
	select
		count( distinct(student_id) ) 
	from
		score
	);
"""

# 14、查询每门课程被选修的次数
"""
select
	c.cname, count(*)
from
	score as s
	inner join course as c on s.course_id = c.cid
group by
	course_id;
"""

# 15、查询只选修了一门课程的学生学号和姓名
"""
select
	sd.sid, sd.sname
from
	score as sc
	inner join student as sd on sc.student_id = sd.sid
group by
	student_id
having
	count(*) = 1;
"""

# 16、查询所有学生考出的成绩并按从高到低排序（成绩去重）
"""
select
	distinct(num)
from
	score
order by
	num desc;
"""

# 17、查询平均成绩大于85的学生姓名和平均成绩
"""
select
	sd.sname, avg(sc.num)
from
	student as sd 
	inner join score as sc on sd.sid = sc.student_id
group by
	sc.student_id
having
	avg(sc.num) > 85;
"""

# 18、查询生物成绩不及格的学生姓名和对应生物分数
"""
select
	sd.sname, sc.num
from
	student as sd
	inner join score as sc on sd.sid = sc.student_id
	inner join course as c on c.cid = sc.course_id
where
	c.cname = "生物"
having
	sc.num < 60;
"""

# 19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名
"""
select
	sd.sname
from
	student as sd 
	inner join score as sc on sd.sid = sc.student_id
	inner join course as c on sc.course_id = c.cid
	inner join teacher as t on c.teacher_id = t.tid
where
	t.tname = "李平"
group by
	sd.sid
order by
	avg(num) desc
limit 1;
"""

# 20、查询每门课程成绩最好的课程id、学生姓名和分数
"""
select
	sc.course_id, sd.sname, sc.num 
from
	score as sc
	left join (
	select
		course_id, max( num ) as max_num 
	from
		score 
	group by
		course_id 
	) as t1 on t1.course_id = sc.course_id
	inner join student as sd on sd.sid = sc.student_id 
where
	num = max_num;
"""

# 21、查询不同课程但成绩相同的课程号、学生号、成绩
"""
select
	s1.course_id as s1_course_id,
	s2.course_id as s2_course_id,
	s1.student_id as s1_student_id,
	s2.student_id as s2_student_id,
	s1.num as s1_num,
	s2.num as s2_num
from
	score as s1,
	score as s2
where
	s1.num = s2.num
	and s1.course_id > s2.course_id;
"""


# 22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称
"""
select
	sd.sname, c.cname 
from
	score as sc
	inner join student as sd on sc.student_id = sd.sid
	inner join course as c on sc.course_id = c.cid 
where
	student_id not in (
	select
		sc.student_id 
	from
		teacher as t
		inner join course as c on t.tid = c.teacher_id
		inner join score as sc on c.cid = sc.course_id 
	where
		t.tname = "李平" 
	);
"""

# 23、查询所有选修了学号为2的同学选修过的一门或者多门课程的同学学号和姓名
"""
select
	sc.student_id, sd.sname 
from
	score as sc
	inner join student as sd on sc.student_id = sd.sid 
where
	course_id in ( select course_id from score where student_id = 2 ) 
	and student_id != 2 
group by
	sd.student_id;
"""

# 24、任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数
"""
select
	sc.course_id, sd.sname, sc.num 
from
	score as sc
	inner join student as sd on sd.sid = sc.student_id 
where
	course_id = (
	select
		course_id 
	from
		score 
	group by
		course_id 
	order by
		count( * ) desc 
	limit 1 
	) 
order by
	num desc
limit 1;
"""