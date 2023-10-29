# ### 人类
class Person():
	def __init__(self,gun):
		self.gun = gun
		
	def fill(self,num):
		# 找弹匣对象中的bulletcount属性填充子弹
		self.gun.bulletbox.bulletcount += num
		"""
		self.gun => 枪对象
		self.gun.bulletbox => 弹匣对象
		self.gun.bulletbox.bulletcount => 弹匣对象里面的子弹数量属性		
		"""
		
	def fire(self,fcount):
		self.gun.shoot(fcount)