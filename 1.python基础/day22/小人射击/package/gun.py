# ### 枪类
class Gun():
	def __init__(self,bulletbox):
		self.bulletbox = bulletbox
		
	# 射击方法
	def shoot(self,firecount):
		# 剩余数量 = 总数量 - 射出的数量
		# self.bulletbox.bulletcount = self.bulletbox.bulletcount - firecount
		
		if self.bulletbox.bulletcount < firecount:
			print("抱歉,你需要上子弹,换个枪")
			
		else:
			self.bulletbox.bulletcount -= firecount
			print(   "蹦ong!!" *  firecount   ,  "剩余的子弹数量是{}".format(self.bulletbox.bulletcount)    )
				
# ak47 = Gun()
# ak47         突突突突突突  
# 加特林      哒哒哒
# 1887霰弹枪  "蹦ong!!"
