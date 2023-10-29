# ### 小人射击
"""面向对象的核心思想: 把对象当做程序的最小单元,让对象去操作一切   """
"""
需求分析: 
	弹匣类:  bulletbox
		属性: bulletcount
		方法: 无

	枪类:    gun
		属性: 弹匣对象
		方法: 射击 shoot

	人类:    person
		属性: 枪对象
		方法: 1.射击,  2.换子弹
"""
# 导入弹匣类 , 枪类  , 人类
from package.bulletbox import BulletBox
from package.gun import Gun
from package.person import Person

# 创建一个弹匣
danxia = BulletBox(10)
print(danxia)

# 创建一个枪
xdq1887 = Gun(danxia)

# 创建一个人
kangyukang = Person(xdq1887)

if __name__ == "__main__":
	# 开枪发射
	kangyukang.fire(5)
	# 上子弹
	kangyukang.fill(3)
	# 开枪发射
	kangyukang.fire(7)
	kangyukang.fire(10)
	























