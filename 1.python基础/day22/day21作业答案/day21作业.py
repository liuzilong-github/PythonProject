# ### 1.完成下列功能:
	# 1.1创建一个人类Person,再类中创建3个成员属性
		# animal = '高级动物'
		# soul = '有灵魂'
		# language = '语言'
	# 1.2在类中定义三个方法,吃饭,睡觉,工作.
	# 1.3在此类中的__init__方法中,给对象封装5个属性: 国家 , 姓名 , 性别 , 年龄 , 身高.
	# 1.4实例化四个人类对象:
		# 第一个人类对象p1属性为:中国,alex,未知,42,175.
		# 第二个人类对象p2属性为:美国,武大,男,35,160.
		# 第三个人类对象p3属性为:你自己定义.
		# 第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3的身高.
	# 1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
	# 1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
	# 1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
	# 1.8 通过p1对象找到类中成员属性animal
	# 1.9 通过p2对象找到类中成员属性soul
	# 2.0 通过p3对象找到类中成员属性language
class Person():
	animal = '高级动物'
	soul = '有灵魂'
	language = '语言'
	
	def __init__(self,country,name,sex,age,height):
		self.country = country
		self.name = name
		self.sex = sex
		self.age = age
		self.height = height
	
	def eat(self):
		print("这是eat方法,{}在吃饭".format(self.name))
	def sleep(self):
		print("这是sleep方法")
	def work(self):
		print("这是work方法")
		
	def info(self):
		print("{}-{}-{}-{}-{}".format(self.country,self.name,self.sex,self.age,self.height))

p1 = Person("中国","alex","未知",42,175)
p2 = Person("美国","武大","男",35,160)
p3 = Person("越南","含笑半步癫","人妖",99,138)
p4 = Person(p1.country , p2.name , p3.sex, p2.age,p3.height)
p4.info()
print("<=====>")
p1.eat()
p2.eat()
p3.eat()
print(p1.animal)
print(p2.soul)
print(p3.language)

# ### 2.通过自己创建类,实例化对象
	#通过调用对象当中的方法,在终端输出如下信息
	#小明，10岁，男，上山去砍柴
	#小明，10岁，男，开车去东北
	#小明，10岁，男，最爱大保健

	#老李，90岁，男，上山去砍柴
	#老李，90岁，男，开车去东北
	#老李，90岁，男，最爱大保健

class MyClass():
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
	
	def info(self):
		strvar = """
{who}，{age}岁，{sex}，上山去砍柴
{who}，{age}岁，{sex}，开车去东北
{who}，{age}岁，{sex}，最爱大保健		
		"""
		print( strvar.format(who=self.name,age=self.age,sex=self.sex) )

obj = MyClass("小明",10,"男")
obj = MyClass("老李",90,"人妖")
obj.info()


# ### 3.模拟英雄联盟写一个游戏人物的类
	#要求:
	#(1) 创建一个 Game_role 的类.
	#(2) 构造方法中给对象封装 name,ad(攻击力),hp(血量).三个属性.
	#(3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
	#例: 实例化一个对象 盖伦,ad为10, hp为100
	#实例化另个一个对象 剑豪 ad为20, hp为80
	#盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.

class Game_role():
	def __init__(self,name,ad,hp):
		self.name = name
		self.ad = ad
		self.hp = hp
	
	def attack(self,obj):
		# 剩余血量 = 剑豪总血量 - 攻击力的伤害
		print('{}攻击{},{}掉了{}血,  还剩{}血'.format(self.name,obj.name ,obj.name,self.ad,obj.hp - self.ad  ))

gailun = Game_role("盖伦",10,100)
yasuo = Game_role("剑豪",20,80)
gailun.attack(yasuo)



# ### 4.请定义一个圆形类,有计算周长和面积的两个方法 (圆的半径通过参数传递给初始化方法)

# ### 5创建AB两个类，A类中有属性abc=5把A类的对象存储在B类对象的成员属性pty中,用B类对象调用出abc这个值.
class A():
	aaa = 100
	
	
class B():
	def __init__(self,obj):
		self.pty = obj

obj1 = A()
obj2 = B(obj1)

# ### 简答题
# 1.类或对象是否能做字典的key        可以!      
# 2.简述python的私有成员是如何实现的  _ 改名策略 _类__私有成员
# 3.私有成员能在类的外部使用么?能在子类中使用么? 不可以  不可以

# ### 读代码,写答案
# 1.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print('666')

# 创建了一个列表,列表中有三个对象(实例)
config_obj_list = [  StarkConfig(1),StarkConfig(2),RoleConfig(3)   ]
for item in config_obj_list:
    print(item.num)


# 2.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    pass
	
# 创建了一个列表,列表中有三个对象(实例)
config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)
print(config_obj_list[0].num)


# 3.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)


# 4.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
config_obj_list[1].run()  
config_obj_list[2].run()  


# 5.读程序写结果.(不执行)
class StarkConfig(object):
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

class AdminSite(object):
    def __init__(self):
        self._registry = {}
    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
print(len(site._registry))  
site.register('range',666)
site.register('shilei',438)
print(len(site._registry))  

site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))
print(len(site._registry))    
print(site._registry)


# 6.读程序写结果.(不执行)
class StarkConfig():
    def __init__(self,num):
        self.num = num
    def changelist(self,request):
        print(self.num,request)
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self,request):
        print(666,self.num)

class AdminSite():
    def __init__(self):
        self._registry = {}
    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))

for k,row in site._registry.items():
    row.changelist(5)
for k,row in site._registry.items():
    row.run()

# 7.读程序写结果.(不执行)
class JustCounter:
	__secretCount = 0
	def count(self):
		print(self.__secretCount) # 获取
		self.__secretCount += 1

	def count3():
		print(JustCounter.__secretCount)
		JustCounter.__secretCount += 1
		print(JustCounter.__secretCount)

class Bars(JustCounter):
	def count2(self):
		print(self.__secretCount)

#  情况一
counter1 = JustCounter()
counter1.count() 
counter1.count() 
JustCounter.count3() 
#  情况二
counter2 = Bars()
counter2.count()
counter2.count()
#  情况三
JustCounter.count3()




















