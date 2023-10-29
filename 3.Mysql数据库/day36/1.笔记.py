# ### part1 表单查询
"""select ... from ... where ... group by ... having ... order by ... limit ... """

"""
# 一.where 条件的使用
	'''
	功能: 对表中的数据进行筛选和过滤
	语法:
		1.判断的符号
		= (!= <> 不等于) > >= < <=
		2.拼接不同的条件的关键字
		and or not
		3.查询对应的区间值
		between 小值 and 大值 [小值, 大值]	 查询两者之间的范围值
		4.查询具体在哪个范围中
		in (1, 22, 333, 444) 指定范围
		5.模糊查询 like % 通配符 _ 通配符
			like "%b"	匹配以b结尾的任意长度的字符串
			like "b%"	匹配以b开头的任意长度的字符串
			like "%b%"	匹配字符串中含有b的任意长度的内容
			like "__b"	匹配总长度为3个字符,任意内容的字符串,并且以b结尾
			like "b_"	匹配总长度为2个字符,任意内容的字符串,并且以b开头
	'''

	# 1.查询部门是sale的所有员工的姓名:
	select emp_name from employee where post = "sale";

	# 2.部门是teacher,收入大于10000的所有数据
	select * from employee where post = "teacher" and salary > 10000;

	# 3.收入在1万到2万之间的所有员工的姓名和收入
	select emp_name, salary from employee where salary between 10000 and 20000;

	# 4.收入不在1万到2万之间的所有员工的姓名和收入
	select emp_name, salary from employee where salary not between 10000 and 20000;

	# 5.查看岗位描述未NULL得员工信息
	# select emp_name from employee where post_comment = null;	# error
	# select emp_name from employee where post_comment = "";	# error
	select emp_name from employee where post_comment is null;

	# 6.查看岗位描述不为NULL的员工信息
	select emp_name from employee where post_comment is not null;

	# 7.查询收入是3000, 4000, 5000, 8300 所有员工的姓名和收入
	select emp_name, salary from employee where salary in (3000, 4000, 5000, 8300);
	select emp_name, salary from employee where salary = 3000 or salary = 4000 or salary = 5000 or salary = 8300;

	# 8.查询收入不是3000, 4000, 5000, 8300 所有员工的姓名和收入
	select emp_name, salary from employee where salary not in (3000, 4000, 5000, 8300);

	# 9.以on结尾的员工姓名搜一下
	select emp_name from employee where emp_name like "%on";
	select emp_name from employee where emp_name like "ji%";
	select emp_name from employee where emp_name like "_le_";

	# 10.统计员工一年的年薪
	select concat("姓名: ": emp_name, "收入: ", salary) from employee;

	# 计算年薪,可以在mysql中使用四则运算符 + - * /
	select concat("姓名: ": emp_name, "收入: ", salary * 12) from employee;
	select concat_ws(" : ", emp_name, salary * 12) from employee;

	# 11.查询部门的种类
	# distinct 返回唯一不同值
	select distinct(post) from employee;

# 二. group by 子句 分组分类
	'''group by 字段,对数据进行分类,by后面接什么字段,select后面就搜什么字段'''
	select sex from employee group by sex;

	# group_concat 按照分组把对应字段拼在一起
	select group_concat(emp_name), post from employee group by post;

	# 聚合函数
		# count 统计总数 *代表所有
		select count(*) from employee;
		# max 统计最大值
		select max(salary) from employee;
		# min 统计最小值
		select min(salary) from employee;
		# avg 统计平均值
		select avg(salary) from employee;
		# sum 统计总和
		select sum(salary) from employee;

	# 1.查询部门名以及各部门的平均薪资
	select avg(salary), post from employee group by post;
	# 2.查询部门名以及各部门的最高薪资
	select max(salary), post from employee group by post;
	# 3.查询部门名以及各部门的最低薪资
	select min(salary), post from employee group by post;
	# 4.查询公司内男员工及女员工的个数
	select count(*), sex from employee group by sex;
	# 5.查询部门名以及部门包含的所有员工名字
	select concat(emp_name), post from employee group by post;
	# 6.可以group by 两个字段,就可以同时搜索两个字段
	select emp_name, post from employee group by post, emp_name;

# 三.having 在数据分类分组之后,对数据进行二次过滤,一般配合group by来使用
	# 找出各部门平均薪资,并且大于10000
	select post, avg(salary) from employee group by post having avg(salary) > 10000;

	# 1.查询各岗位内包含的员工个数小于2的岗位名,岗位内包含员工名字,个数
	select post, group_concat(emp_name), count(*) from employee group by post having count(*) < 2;

	# 2.查询各岗位平均薪资小于10000的岗位名,平均薪资
	select post, avg(salary) from employee group by post having avg(salary) < 10000;

	# 3.查询各岗位平均薪资大于1万且小于2万的岗位名,平均薪资
	select post, avg(salary) from employee group by post having avg(salary) between 10000 and 20000;
	select post, avg(salary) from employee group by post having avg(salary) > 10000 and avg(having) < 20000;

# 四.order by 排序,按照某字段排序
	# order by age asc (升序)
	# order by age desc (降序)
	# 按照年龄从小到大排序
	select * from employee order by age;
	# 按照年龄从大到小排序
	select * from employee order by age desc;

	# 1.查询所有员工信息,先按照age升序排序,如果age相同则按照hire_date降序排序
	select * from employee order by age asc, hire_data desc;

	# 2.查询各岗位平均薪资大于10000的岗位名,平均薪资,结果按平均薪资升序排列
	select post, avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary);

	# 3.查询各岗位平均薪资大于10000的岗位名,平均薪资,结果按平均薪资降序排列
	select post, avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc;

# 五.limit 限制查询条数(应用在分页)
	'''limit m,n m代表从第几条数据开始查, n 代表查几条 m=0 代表的是第一条数据'''
	select * from employee limit 0,10	# 0代表的是第一条数据
	select * from employee limit 10,10	# 10代表的是第十一条数据
	select * from employee limit 20,10	# 20代表的是第二十一条数据

	# limit + num num => 搜索的条数
	select * from employee limit 1;
	# 搜索这个表里面的最后一条数据
	select * from employee order by id desc limit 1;
	# 搜索这个表里面的最后五条数据
	select * from employee order by id desc limit 5;

# 六.mysql 当中可以使用正则表达式(不推荐,效率低)
	select * from employee where emp_name regexp ".*on$";  # mysql中无法识别?号
	select * from employee where emp_name regexp "^程.*";
	select * from employee where emp_name regexp "^程.*金";
"""

# ### part2 多表查询
"""
	# 1.内联接: 
		# inner join: 两表或者多表之间,把满足条件的所有数据查询出来(多表之间共同拥有的数据会被查询出来)
		# 两表联查
		select 字段 from 表1 inner join 表2 on 必要的关联条件
		# 多表联查
		select 字段 from 表1 inner join 表2 on 必要的关联条件1 inner join 表3 on 必要的关联条件2

	select * from employee inner join department on employee.dep_id = department.id;
	# as 起别名
	select * from employee as e inner join department as d on e.dep_id = d.id;
	# 也可以省略as (不推荐)
	select * from employee  e inner join department d on e.dep_id = d.id;

	# where 写法默认写的室内链接(等同于inner join)
	select * from employee, department where employee.dep_id = department.id;
	select * from employee as e, department as d where e.dep_id = d.id;

	# 2.外联接:
		# left join 左连接 / right join 右联接
	# (1) left join左联接: 以左表为主,右表为辅,完整查询左表所有数据,右表没有的数据补null
	select * from employee left join department on employee.dep_id = department.id;
	# (2) right join右联接: 以右表为主,左表为辅,完整查询游标所有数据,左表没有的数据补null
	select * from employee right join department on employee.dep_id = department.id;

	# 3.全联接:
		# union
	select * from employee left join department on employee.dep_id = department.id
	union
	select * from employee right join department on employee.dep_id = department.id;
"""

# ### part3 子查询
"""
	'''
	子查询: 嵌套查询
		(1) sql语句当中又嵌套了另外一条sql,用括号()进行包裹,表达一个整体
		(2) 一般用在from子句,where子句身后,表达一个条件或者一个表
		(3) 速度快慢: 单表查询 > 联表查询 > 子查询;
	'''

	# 一.找出平均年龄大于25岁以上的部门
	# (1) where
	select 
		d.id, d.name
	from
		employeem as e, department as d
	where
		e.dep_id = d.id
	group by
		d.id, d.name
	having
		avg(e.age) > 25;

	# (2) inner join
	select
		d.id, d.name
	from
		employee as e inner join department as d on e.dep_id = d.id
	group by
		d.id, d.name
	having
		avg(e.age) > 25;

	# (3) 子查询
	# 1.先找出平均年龄大于25岁的部门id
	select dep_id from employee group by employee.dep_id having avg(age) > 25;
	# 2.通过部门的id找部门的名字
	select name from department where id in (201, 202);
	# 3.综合拼接
	select id, name from department where id in (select dep_id from employee group by employee.dep_id having avg(age) > 25);

	# 二.查看技术部门员工姓名
	# (1) 普通 where 查询
	select
		e.id, e.name
	from
		employee as e, department as d
	where
		e.dep_id = d.id
		and
		d.name = "技术";

	# (2) inner join
	select
		e.id, e.name
	from
		employee as e inner join department as d on e.dep_id = d.id
	where
		d.name = "技术";

	# (3) 子查询
	# 1.找技术部门对应的id
	select id from department where name = "技术";
	# 2.通过id找员工姓名
	select name from employee where dep_id = 200;
	# 3.综合拼接
	select id, name from employee where dep_id = (select id from department where name = "技术");

	# 三.查看哪个部门没有没有员工

	# 联表写法
	select
		d.id, d.name
	from
		department as d left join employee as e on d.id = e.dep_id
	where
		e.dep_id is null;

	# 1.找员工在哪些部门(200, 201, 202, 204)
	select dep_id from employee group by dep_id;
	# 2.把不在该部门的员工找出来
	select id from department where id not in (200, 201, 202, 204);
	# 3.综合拼接
	select id, name from department where id not in (select dep_id from employee group by dep_id);

	# 四.查询大于平均年龄的员工名与年龄;
	# 假设已经知道了平均年龄
	select name, age from employee where age > 30;
	# 计算平均年龄
	select avg(age) from employee;
	# 综合拼接
	select name, age from employee where age > (select avg(age) from employee);

	# 五.把大于其本部门平均年龄的员工和姓名查出来
	# 1.先计算本部门平均年龄是多少
	select dep_id, avg(age) from employee group by dep_id;
	# 2.把查询的各部门平均年龄和employee进行联表,变成一张大表,最后做单表查询
	select
		*
	from
		employee as t1 inner join (1号表查出来的数据) as t2 on t1.dep_id = t2.dep_id;
	# 3.综合拼接
	select
		*
	from
		employee as t1 inner join (select dep_id, avg(age) as avg_age from employee group by dep_id) as t2 on t1.dep_id = t2.dep_id;
	# 最后做一次单表查询,让 age > 平均值
	select
		*
	from
		employee as t1 inner join (select dep_id, avg(age) as avg_age from employee group by dep_id) as t2 on t1.dep_id = t2.dep_id
	where
		age > avg_age;

	# 六.查询每个部门最新入职的那位员工(利用上一套数据表进行查询)
	# 1.找各部门的最新入职时间
	select post, max(hire_date) as max_date from employee group by post;
	# 2.把子查询搜索出来的结果作为一张表和employee这个表做联表,把max_date拼接在employee这个表中,变成一张大表,最后做一次单表查询
	select
		*
	from
		employee as t1 inner join (1号数据) as t2 on t1.post = t2.post
	where
		t1.hire_date = t2.max_date
	# 3.综合拼接
	select
		*
	from
		employee as t1 inner join (select post, max(hire_date) as max_date from employee group by post;) as t2 on t1.post = t2.post
	where
		t1.hire_date = t2.max_date;

	# 七.带EXISTS关键字的子查询
	'''
		exists 关键字, 表达存在, 应用在子查询中
			如果内层sql,能够查询到数据,返回True,外层sql执行相应的sql语句
			如果内层sql,查询不到数据,返回False,外层sql不执行sql语句
	'''
	select * from employee where exists (select * from employee where id = 1);
	select * from employee where exists (select * from employee where id = 100000);

	'''
	总结:
		子查询可以单独作为临时数据,作为一张表或者一个字段,通过()进行包裹,表达一个整体;
		一般用在from, where, select 子句后面
		可以通过查询出来的数据和另外的表做联表变成更大的一张表
		最后做单表查询,达到目的;
	'''
"""







