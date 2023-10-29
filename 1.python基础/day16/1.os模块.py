# ### os模块
import os

# system()	在python中执行系统命令
os.system("ifconfig")	# linux
# os.system("ipconfig")		windows
# os.system("rm -rf ceshi1.txt")

# popen()	执行系统命令返回对象,通过read方法读出字符串
"""
obj = os.popen("ipconfig")
print(obj)
print(obj.read())
"""

# listdir() 获取指定文件夹中所有内容的名称列表 ***
lst = os.listdir()
print(lst)

# getcwd() 获取当前文件所在的默认路径 ***
# 路径
res = os.getcwd()
print(res)

# 路径 + 文件名 ***
print(__file__)

# chdir() 修改当前文件工作的默认路径
os.chdir("/home/wangwen/mywork")
os.system("touch 2.txt")

# environ 获取或修改环境变量
"""
[windows]
(1)邮件qq属性找路径
(2)右键我的电脑=>高级系统设置=>环境变量=>path 打开环境变量添加对应路径
(3)cmd => QQScLauncher

[linux]
(1)在家目录中创建个文件夹,里面创建个文件wangwen,写入ifconfig
(2)增加wangwen的可执行权限 chmod 777 wangwen,测试一下 sudo ./wangwen
(3)添加环境变量在os.environ["PATH"] 中拼接wangwen所有的绝对路径
(4)os.system("wangwen")
"""
print(os.environ["PATH"])
"""
environ(
{
'PATH': '/usr/bin:/bin:/usr/sbin:/sbin', 
'__CFBundleIdentifier': 'com.jetbrains.pycharm', 
'PYTHONPATH': '/Users/liuzilong/PycharmProjects/learn', 
'SHELL': '/bin/zsh', 
'PYTHONIOENCODING': 'UTF-8', 'USER': 'liuzilong', 
'TMPDIR': '/var/folders/1t/8j41kb3x6yn46k3g7jbps71c0000gn/T/', 
'COMMAND_MODE': 'unix2003', 
'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.edB9NOpzlQ/Listeners', 
'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', 
'__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 
'LOGNAME': 'liuzilong', 'LC_CTYPE': 'zh_CN.UTF-8', 
'XPC_SERVICE_NAME': 'application.com.jetbrains.pycharm.453996.14520999', 
'PWD': '/Users/liuzilong/PycharmProjects/learn/test', 
'PYCHARM_HOSTED': '1', 'HOME': '/Users/liuzilong'
}
)
"""
os.environ["PATH"] += ":/home/wangwen/mywork"
os.system("wangwen")


# os模块
# name 获取系统标识	linux,mac => posix		windows => nt
print(os.name)
# sep 获取路径分割符	linux,mac => /		windows => \  ***
print(os.sep)
# linesep 获取系统的换行符号	linux,mac => \n 	windows => \r\n 或 \n
print(repr(os.linesep))











