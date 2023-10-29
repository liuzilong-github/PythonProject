转换规律：
	如果是一个正数：原码 = 反码 = 补码
	如说是一个负数：原码与补码之间，互为取反加1
					原码 = 补码取反加1	给补码求原码
					补码 = 原码取反加1	给原码求补码
					
					
原码特点：（第一位是符号位，用来表示正负）
		第一位是0，000000001	表示数字正1
		第一位是1，100000001	表示数字负1
补码特点：
		正数高位都是0
		负数高位都是1
反码：二进制码0变1,1变0叫做反码，原码与补码之间的转换形式。（首位符号位不取反）


<=============================================================>
5 + (-3) = 2
5
原码：101
反码：101
补码：101

-3
原码：1000 ... 0011
反码：1111 ... 1100
补码：1111 ... 1101

0000 ... 0101
1111 ... 1101
0000 ... 0010 => 2（返回的数是正数：原码 = 反码 = 补码）


-5 + 3 = -2
-5
原码：1000 ... 0101
反码：1111 ... 1010
补码：1111 ... 1011

3
原码：011
反码：011
补码：011

1111 ... 1011
0000 ... 0011
1111 ... 1110 => -2（返回的数是负数：原码 = 补码取反加1）

# 给你补码求原码（用来显示数据）
补码：1111 ... 110
反码：1000 ... 001
原码：1000 ... 010 => -2