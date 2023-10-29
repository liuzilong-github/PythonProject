#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/8/23 10:00
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : sql练习.py
@Software: PyCharm

'''


# 25、查询姓“张”的学生名单；
'''
SELECT
    sname 
FROM
    student 
WHERE
    sname LIKE '张%';
'''

# 26、查询同名同姓学生名单，并统计同名人数；
'''
SELECT
    sname,
    count( * ) AS count 
FROM
    student 
GROUP BY
    sname 
HAVING
    count( * ) >= 2;
'''

# 27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
'''
SELECT
    course_id,
    avg( num ) AS avg_num 
FROM
    score 
GROUP BY
    course_id 
ORDER BY
    avg_num ASC,
    course_id DESC;
'''

# 28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
'''
SELECT
    student.sid,
    student.sname,
    avg( score.num ) AS avg_num 
FROM
    score
    INNER JOIN student ON score.student_id = student.sid 
GROUP BY
    score.student_id 
HAVING
    avg_num > 85;
'''

# 29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
'''
SELECT
    student.sname,
    score.num 
FROM
    score
    INNER JOIN student ON score.student_id = student.sid 
WHERE
    score.course_id = ( SELECT cid FROM course WHERE cname = '生物' ) 
    AND score.num < 60; 
'''

# 30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；
'''
SELECT
    student.sid,
    student.sname 
FROM
    score
    INNER JOIN student ON score.student_id = student.sid 
WHERE
    score.course_id = 3
    AND score.num > 80; 
'''

# 31、求选了课程的学生人数;
'''
SELECT
    count( DISTINCT student_id ) AS count 
FROM
    score;
'''

# 32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
'''
SELECT
    student.sname,
    score.num 
FROM
    score
    INNER JOIN student ON score.student_id = student.sid 
WHERE
    score.course_id in (
    SELECT
        course.cid 
    FROM
        teacher
        INNER JOIN course ON teacher.tid = course.teacher_id 
    WHERE
        tname = '李平老师' 
    )
ORDER BY
    score.num DESC 
    LIMIT 1;
'''

# 33、查询各个课程及相应的选修人数；
'''
SELECT
    course.cname,
    count( * ) AS count 
FROM
    score
    INNER JOIN course ON score.course_id = course.cid 
GROUP BY
    score.course_id;
'''

# 34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
'''
SELECT DISTINCT
    s1.course_id AS s1_course_id,
    s1.num AS s1_num,
    s2.course_id AS s2_course_id,
    s2.num AS s2_num 
FROM
    score AS s1,
    score AS s2 
WHERE
    s1.course_id != s2.course_id 
    AND s1.num = s2.num;
'''

# 35、查询每门课程成绩最好的前两名；
'''
SELECT
    score.sid,
    score.course_id,
    score.num,
    T.first_num,
    T.second_num 
FROM
    score
    LEFT JOIN (
    SELECT
        sid,
        (
        SELECT
            num 
        FROM
            score AS s2 
        WHERE
            s2.course_id = s1.course_id 
        ORDER BY
            num DESC 
            LIMIT 0,
            1 
        ) AS first_num,
        (
        SELECT
            num 
        FROM
            score AS s2 
        WHERE
            s2.course_id = s1.course_id 
        ORDER BY
            num DESC 
            LIMIT 1,
            1 
        ) AS second_num 
    FROM
        score AS s1 
    ) AS T ON score.sid = T.sid 
WHERE
    score.num <= T.first_num AND score.num >= T.second_num;
'''

# 36、检索至少选修两门课程的学生学号；
'''
SELECT
    student_id 
FROM
    score 
GROUP BY
    student_id 
HAVING
    count( * ) >= 2;
'''

# 37、查询全部学生都选修的课程的课程号和课程名；
'''
SELECT
    score.course_id,
    course.cname 
FROM
    score
    INNER JOIN course ON score.course_id = course.cid 
GROUP BY
    course_id 
HAVING
    count( * ) = ( SELECT count( * ) FROM student );
'''

# 38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
'''
SELECT
    sid,
    sname 
FROM
    student 
WHERE
    student.sid NOT IN (
    SELECT DISTINCT
        ( score.student_id ) 
    FROM
        score
    WHERE
        course_id IN (
        SELECT
            course.cid 
        FROM
            course
            INNER JOIN teacher ON course.teacher_id = teacher.tid 
        WHERE
            teacher.tname = '李平老师' 
        )
    );
'''

# 39、查询两门以上不及格课程的同学的学号及其平均成绩；
'''
SELECT
    student_id,
    avg( num ) AS avg_num 
FROM
    score 
WHERE
    num < 60 GROUP BY student_id HAVING count( * ) >= 2;
'''

# 40、检索“004”课程分数小于60，按分数降序排列的同学学号；
'''
SELECT
    student_id 
FROM
    score 
WHERE
    course_id = 4 
    AND num < 60 
ORDER BY
    num DESC;
'''

# 41、删除“002”同学的“001”课程的成绩；
'''
DELETE 
FROM
    score 
WHERE
    student_id = 2 
    AND course_id = 1;
'''
