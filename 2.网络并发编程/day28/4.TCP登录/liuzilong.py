#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/2/14 09:39
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : test.py
@Software: PyCharm

'''
import json


dic = {"file_path": "//Users//liuzilong//Documents//\u4e2a\u4eba//PythonProject//1.python\u57fa\u7840//day22", "file_name": "1.\u00a0\u591a\u6001.py", "file_msg": "# ### \u591a\u6001: \u4e0d\u540c\u7684\u5b50\u7c7b\u5bf9\u8c61\u8c03\u7528\u76f8\u540c\u7684\u7236\u7c7b\u65b9\u6cd5,\u5f97\u5230\u4e0d\u540c\u7684\u6267\u884c\u7ed3\u679c\n\"\"\" \u7ee7\u627f \u91cd\u5199 \"\"\"\n\nclass Soldier():\n\tdef attack(self):\n\t\tpass\n\n\tdef back(self):\n\t\tpass\n\n# \u9646\u519b\nclass Army(Soldier):\n\tdef attack(self):\n\t\tprint(\"[\u9646\u519b]\u5f00\u5766\u514b\u88c5\u7532\u90e8\u961f,\u5f00\u5927\u70ae\u8f70\u70b8\u654c\u65b9\u6839\u636e\u5730,\u62fc\u523a\u5200,\u624b\u6495\u9b3c\u5b50\")\n\n\tdef back(self):\n\t\tprint(\"[\u9646\u519b]\u4e3a\u4e86\u4e00\u6761\u6027\u547d,\u591c\u884c\u516b\u767e,\u65e5\u884c\u4e00\u5343,\u56de\u5bb6\")\n\n# \u6d77\u519b\nclass Navy(Soldier):\n\tdef attack(self):\n\t\tprint(\"[\u6d77\u519b]\u5f00\u822a\u7a7a\u6bcd\u8230,\u6254\u9c7c\u53c9,\u6492\u7f51\u6346\u4f4f\u654c\u4eba,\u6536


res = json.dumps(dic)
print(res)
res2 = json.loads(res)
print(res2)
