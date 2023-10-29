# ### 进度条
import time
"""
[###################################] 100%
[##############                     ] 40%
[#############################      ] 80%
"""

# (1) 定义进度条样式
# print("[%-50d]" % ("#"))
# print("[%-50d]" % ("###############"))
# print("[%-50d]" % ("#############################"))

# (2) 让进度条动起来
# strvar = ""
# for i in range(50):
# 	time.sleep(0.1)
# 	strvar += "#"
# 	print("\r[%-50s]" % strvar, end="")

# (3) 加上百分比
# 显示进度条
def my_percent(percent):
	if percent > 1:
		percent = 1
	# 打印对应的#号数量 * "#" => 字符串#号效果
	strvar = int(percent * 50) * "#"
	# 进行打印 %% => %
	print("\r[%-50s] %d%%" % (strvar, percent * 100), end="")

# 接收数据
recv_size = 0
total_siza = 1000
while recv_size < total_siza:
	time.sleep(0.1)
	recv_size += 10
	percent = recv_size / total_siza
	my_percent(percent)
