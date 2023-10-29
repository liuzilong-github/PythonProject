

## 使用orm执行原生的sql语句

方式1: 使用raw方法

```python
ret = models.Book.objects.raw('select * from app01_book;')	# raw方法只能操作本表数据
# <RawQuerySet: select * from app01_book;>
# 得到的是RawQuerySet类型数据,也是可迭代数据,里面放的是每条记录的模型类对象
for i in ret:
	print(i.title)
```

方式2: 使用connection模块

```python
from django.db import connection

# conn = pymqsql.connect(host=...)
cursor = connection.cursor()
cursor.execute('select * from app01_book;')
ret = cursor.fetchall()
print(ret)
```


## django外部脚本调用django环境来操作(脱离django,单独运行的文件就叫做外部脚本)

```python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_orm.settings")

import django

django.setup()

from app01 import models

ret = models.Book.objects.all()
print(ret)
```


## 锁和事务

### 加锁

```python
# 原生sql手动加锁
select * from app01_book where id=1 for update;

# orm加锁
models.Book.objects.filter(id=1).select_for_update()

```
但是查询加锁,都要在事务中才能提现其效果

### 加事务

用法1: 给函数做装饰器来使用

```python
from django.db import transaction

@transaction.atomic
def viewfunc(request):
	d1 = {'name': 'chao'}
	username = request.GET.get('name')
	sid = transaction.savepoint()	# 创建保存点
	models.Book.objects.filter(id=1).select_for_update()
	do_stuff()
	try:
		d1[username]
	except:
		# 保存点一般是代码运行过程中,出了问题,需要手动回滚事务时使用
		transaction.savepoint_rollback(sid)	  # 回滚到保存点
		return HttpResponse('别瞎搞,滚犊子')
```

用法2: 作为上下文管理器来使用

```python
from django.db import transaction

def viewfunc(request):
	do_stuff()	# sql不在事务里

	with transaction.atomic():
		do_more_stuff()	 # sql在事务里

	do_other_stuff()	# sql不在事务里
```

#### 事务的四大特性

```text
原子性: 多个sql语句捆绑到一起,要么都成功,要么都失败;

一致性: 事务执行前后,数据保持一致(我减100,你加100,别多加也别少加);

隔离性: 一个事务的执行和另一个事务的执行是互相隔离的;

持久性: 事务一旦提交,就永久刷到磁盘上了;
```



# ajax

特点: 异步提交,局部刷新

简单的登录认证示例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
	<h1>32期皇家会所会员登录界面</h1>
	<form action="" method="post">
		<div>{{ error }}</div>
		用户名: <input type="text" name="username" value="{{ username }}">
		密码: <input type="password" name="password" value="{{ password }}">
		<input type="submit">
	</form>

	<hr>
	<h1>32期皇家会所会员ajax登录页面</h1>
	用户名: <input type="text" id='username'>
	密码: <input type="password" id='password'>
	<button id='btn'>ajax提交</button>
	<h1 id="ajax_error" style="color:red;"></h1>
</body>
<script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
	$('#btn').click(function(){
		var uname = $('#username').val();
		var password = $('#password').val();
		$.ajax({
			type:'post',	// 请求方法
			url:'/login/',
			data:{xname:uname, pwd:password},	// xname:chao,pwd:123	request.POST.get('xname')
			success:function(res){
				// res接收的是请求成功之后的响应结果,ajax如何判断请求成功还是失败,由后台决定
				// 后台响应的状态码如果是2xx/3xx等,ajax发现应用状态为2xx/3xx等,ajax就知道请求成功了
				// ajax会自动触发success对应的回调函数,并且将接收到响应传值给了函数
				console.log('success>>>>', res);
			},
			error:function(error){
				// 后台响应的状态码为4xx/5xx表示请求失败或者服务器出现问题了,没有正常响应本次请求的内容
				// ajax接收到响应,如果发现响应的状态码为4xx/5xx,那么ajax会自动触发error对应的函数,并将响应结果传给函数作为参数
				console.log('error>>>>>>', errro)
				// $('#ajax_error').text('输入的用户名或者密码有误!')
				$('#ajax_error').text(error.responseText)
			}
		})
	})
</script>
</html>
```


### JsonResponse

JsonResponse(非字典数据, safe=False)

json序列化,并且响应头携带: content_type:application/json












