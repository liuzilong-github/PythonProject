"""
1、计算机文件单位大小
b = bit    位（比特）
B = Byte    字节

1Byte = 8 bit   # 一个字节等于8位  可以简写成 1B = 8b
1KB = 1024B
1MB = 1024KB
1GB = 1024MB
1TB = 1024GB
1PB = 1024TB
1EB = 1024PB

2、进制的转换
二进制：由2个数字组成,有0 和 1  			   例:  0b101 
八进制：由8个数字组成,有0,1,2,3,4,5,6,7        例:  0o127
十进制：有10个数字组成,有0,1,2,3,4,5,6,7,8,9   例:  250
十六进制：有16个数字组成,有0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f(字母大小写都可以,分别代表10,11,12,13,14,15) 例:0xff  0Xff  0XFF

# 二进制转换为十进制：
#例:	0b10100101  
运算:1* 2^0 + 0* 2^1 + 1* 2^2 + 0* 2^3 + 0* 2^4 + 1* 2^5 + 0* 2^6 + 1* 2^7= 
1 + 0 + 4 + 0 + 0 + 32 + 0 + 128 = 165

# 八进制转换为十进制：
#例:	0o127
运算:7*8^0 + 2*8^1 + 1*8^2 = 7+16+64 = 87

# 十六进制转换为十进制：
#例:	0xff
运算:15*16^0 + 15*16^1 = 255

# 十进制转化为二进制：
426 => 0b110101010  
运算过程:   用426除以2,得出的结果再去不停地除以2,
			直到除完最后的结果小于2停止,
			在把每个阶段求得的余数从下到上依次拼接完毕即可
			
# 十进制转化为八进制：
426 => 0o652
运算过程:   用426除以8,得出的结果再去不停地除以8,
			直到除完最后的结果小于8停止,
			在把每个阶段求得的余数从下到上依次拼接完毕即可
			
# 十进制转换为十六进制：
运算过程:   用426除以16,得出的结果再去不停地除以16,
			直到除完最后的结果小于16停止,
			在把每个阶段求得的余数从下到上依次拼接完毕即可
"""

