# ### 命名关键字参数
"""
(1) def func(a,b,*,c,d)	跟在*号后面的c和d是命名关键字参数
(2) def func(*args,e,**kwargs)	加在*args和**kwargs之间的参数都是命名关键字参数

命名关键字参数:在调用函数时,必须使用关键字实参的形式来进行调用;
"""

# 定义方法一
def func(a,b,*,c,d):
	print(a,b)
	print(c,d)

# 必须指定关键字实参,才能对命名关键字形参进行赋值
func(1,2,c=3,d=4)

# 定义方法二:
def func(*args,e,**kwargs):
	print(args)
	print(e)
	print(kwargs)
func(1,2,3,4,a=1,b=2,e=3)

# ### 星号的使用
"""
* 和 ** 如果在函数的定义出使用:
	*	把多余的普通实参打包成元组
	**	把多余的关键字实参打包成字典

* 和 ** 如果在函数的调用处使用:
	*	把元组或者列表进行解包
	**	把字典进行解包
"""

def func(a,b,*,c,d):
	print(a,b)
	print(c,d)

tup = (1,2)
# 函数的调用处 *号用法
func(*tup,c=3,d=4)	# func(1,2,c=3,d=4)

# 函数的调用处 **号用法
dic={"c":3,"d":4}
func(1,2,**dic)		# func(1,2,c=3,d=4)

# 综合写法
tup = (1,2)
dic = {"c":3,"d":4}
func(*tup,**dic)

# 定义成如下形式,可以收集所有的实参
def func(*args,**kwargs):
	pass

# 总结:当所有的形参都放在一起的时候,顺序原则
"""
	普通形参 => 默认形参 => 普通收集形参 => 命名关键字形参 => 关键字收集形参
"""

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 以上两个函数,打印结果
# (一)
f1(1,2)	# a=1,b=2,c=0,args=(),kw={}
f1(1,2,c=3)	# a=1,b=2,c=3,args=(),kw={}
f1(1,2,3,"a","b")	# a=1,b=2,c=3,args=(a,b),kw={}
f1(1,2,3,"a","b",x=99)	# a=1,b=2,c=3,args=(a,b),kw={"x":99}
f2(1,2,d=99,ext=None)	# a=1,b=2,c=0,d=99,kw={ext:None}

# (二)
args = (1,2,3,4)
kw ={"d":99, "x":"#"}
# f1(1,2,3,4,d=99,x=#)
f1(*args,**kw)	# a=1,b=2,c=3,args=(4,),kw={d:99,x:#}

# (三)
myargs = (1,2,3)
mykw = {"d":88, "x":#}
# f2(1,2,3,d=88,x=#)
f2(*myargs,**mykw)	# a=1,b=2,c=3,d=88,kw={x:#}

# (四)
def f1(a, b, c=0, *args,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    print(d)

f1(1,2,3,"a","b",d=67,x=99,y=77)
# a=1,b=2,c=3,args=(a,b),kw={x:99,y:77}
# d=67




















































