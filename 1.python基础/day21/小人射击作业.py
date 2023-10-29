
class CartridgeClip():

	def __init__(self, bullet):
		self.bullet = bullet

	def cartridge_clip(self):
		print("{}装到弹夹".format(self.bullet))


class Gun():

	def __init__(self, cartridge_clip):
		self.cartridge_clip = cartridge_clip

	def gun(self):
		print("{}装到枪里".format(self.cartridge_clip))


class Shooting():

	def shooting(self):
		cartridge_clip = CartridgeClip("10发子弹")
		gun = Gun("弹夹")
		print("{}装到{}里,{}装到枪里,开始射击".format(cartridge_clip.bullet, gun.cartridge_clip, gun.cartridge_clip))
		cartridge_clip.cartridge_clip()
		print("更换弹夹完成")


shooting = Shooting()
shooting.shooting()