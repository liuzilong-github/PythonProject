

## url别名反向解析

url.py

```python
	url(r'^book/', views.books, name='books'),	# name 给路径起别名
	url(r'^add_book/v1/', views.AddBook.as_view(), name='add_book'),
	url(r'^edit_book/(\d+)/', views.EditBook.as_views(), name='edit_book'),
	url(r'^del_book/(?P<book_id>\d+)/', views.del_book, name='del_book')
```

视图函数中反向解析别名路径的方法:

```python
	print(reverse('books'))		# /books/
	# reverse('别名')来反向解析别名对应的路径
	print(reverse('add_book'))	# /add_book/v1/
	# 当url用的是无名分组参数时,reverse反向解析路径用args来传参
	print(reverse('edit_book', args=(3, )))		# /edit_book/2/
	# 当url用的是有名分组参数时,reverse反向解析路径用kwargs来传参
	print(reverse('del_book', kwargs={'book_id': 3, }))
```

html模版渲染反向解析别名路径的方法:

```html
	<a href="{% url 'add_book' %}" class="btn btn-primary">添加数据</a>
	<a href="{% url 'edit_book' book_id %}" class="btn btn-warning">编辑</a>		<!-- 传参解析,多个参数用空格分隔 -->
	<a href="{% url 'del_book' book_id=book.id %}" class="btn btn-danger">删除</a>
	<a href="{% url 'del_book' book.id %}" class="btn btn-danger">删除</a>
```

redirect使用别名路径的方法:

```python
# 两种方式
# return redirect(reverse('books'))
return redirect('books')	# 直接写别名
```


## url 路由分发

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^app01/', include('app01.urls')),	  # app01/urls.py
	url(r'^app02/', include('app02.urls')),	  # app02/urls.py
	url(r'^app03/', include('app02.urls')),	  # app03/urls.py

	# /app01/index/
]
```

在每个应用下创建urls.py文件,写每个应用自己的路径

app01/urls.py

```python
from django.conf.urls import url
from app01 import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
]
```

app02/urls.py

```python
from django.conf.urls import url
from app02 import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
]
```

app03/urls.py

```python
from django.conf.urls import url
from app03 import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
]
```

注意:
当用户访问的路径为 /app01/index/, 那么会先找到总路由,总路由先匹配路径前缀,匹配好之后,就找到对应的应用下面的urls.py文件中的路径来匹配剩余部分路径,然后执行对应的视图函数.


## 命名空间

总路由写法

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^app01/', include('app01_urls', namespace='app01'))	# app01/urls.py
	url(r'app02/', include('app02.urls', namespace='app02')),	# app02/urls.py
	url(r'app03/', include('app03.urls', namespace='app03')),	# app03/urls.py
]
```

在视图函数中使用别名反向解析的写法:

```python
	print(reverse('app03:index'))	# 命名空间名称:别名名称
```

在html模版渲染反向解析别名路径的方法:

```html
	<a href="{% url 'app01:edit_book' book.id %}" class="btn btn-warning">编辑</a>
```


## F查询

```python
from django.db.models import F, Q

# 查询一下点赞数大于评论数的所有书籍
books = models.Book.objects.all()
books_list = []
for book in books:
	if book.dianzan > book.comment:
		books_list.append(book)

books = models.Book.objects.filter(dianzan__gt=F('comment'))	# F('属性名称')
print(books.values('title'))

# 所有书籍价格上调10块钱
books = models.Book.objects.all()
for book in books:
	book.price += 10
	book.save()

models.Book.objects.all().update(price=F('price' + 10))	# 支持四则运算
```

## Q查询

```python
from django.db.models import F, Q

# Q查询: 多条件查询的时候用的多
# | -- or	& -- and	~ -- not
# 查询一下点赞数大于10并且评论数大于10的所有书籍
models.Book.objects.filter(Q(dianzan__gt=10) & Q(comment__gt=10)).values('title')
models.Book.objects.filter(dianzan__gt=10, comment__gt=10)

# 查询一下点赞数大于10或者评论数大于10的所有书籍
ret = models.Book.objects.filter(Q(dianzan__gt=10) | Q(comment__gt=10)).values('title')
print(ret)

# 查询一下点赞数大于10或者评论数大于10的并且价格大于30的所有书籍
ret = models.Book.objects.filter(Q(Q(dianzan__gt=10 | Q(comment__gt=10)) & Q(price__gt=30)).values('title')
ret = models.Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)), price__gt=30).values('title')
# Q(dianzan__gt=10) | Q(comment__gt=10)	通过连接符号连接的Q查询条件,算是一组查询条件
print(ret)

# 查询一下点赞数大于10或者评论数大于10的并且价格小于等于30的所有书籍
ret = models.Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)) & ~Q(price__gt=30)).values('title')
```















