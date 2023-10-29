#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/2/14 14:17
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : 2.client_demo.py
@Software: PyCharm

'''

import socket
import os
import json
import struct
import hashlib
"""
利用socketserver实现多用户上传下载
"""
sock = socket.socket()
sock.connect(('127.0.0.1', 8000))

while True:
    cmd = input("请输入要操作的命令/put-上传/down-下载>>>>:")
    if cmd == "exit":
        sock.send(cmd.encode('utf-8'))
        break
    try:
        action, filename = cmd.strip().split(" ")
        print(action, filename)
        if action =="get":
            data_dict = {'action': action, 'filename': filename}

            # 转换成json字符串进行传递
            data_dict_json = json.dumps(data_dict)
            # 为了防止发生黏包，将data_dict_json的大小使用struct压包传到服务端，再传送数据过去
            data_dict_json_pack = struct.pack("i", len(data_dict_json))
            sock.send(data_dict_json_pack)
            sock.send(data_dict_json.encode('utf-8'))
            # 接收服务端返回的状态码
            code = sock.recv(1024)
            print(code)
            if code == b'201':
                print("连接服务端成功，进行下载")
                data = sock.recv(4)
                if data == "exit":
                    break
                # 先获取客户端传来的pack压缩包然后进行unpack解压
                data_json_unpack = struct.unpack("i", data)[0]
                print(data_json_unpack)
                print("断点1===================")
                #根据unpack获取的元组中的数字长度，再去内存缓冲区取data_json_unpack长度的数据，即客户端第二次send过来的json字符串
                data_json_unpack_recv = sock.recv(data_json_unpack)
                print(data_json_unpack_recv)
                file_info = json.loads(data_json_unpack_recv)
                print('file_info', file_info)
                # 进行接收处理客户端上传的文件
                print("断点2===================")
                action1 = file_info.get('action')
                filename1 = file_info.get('filename')
                data_fize = file_info.get('data_fize')
                client_md51 = file_info.get('client_md5')
                print(action1, filename1, data_fize, client_md51)

                obj = hashlib.md5(b'yanglongyue')
                with open("down/" + filename1, 'wb') as f:
                    data_fize_len = 0
                    while data_fize_len < data_fize:
                        data_len = sock.recv(1024)
                        data_fize_len += len(data_len)
                        f.write(data_len)
                        obj.update(data_len)
                        print("总大小%s,已下载%s" % (data_fize, data_fize_len))
                    server_md5 = obj.hexdigest()
                    print(server_md5)
                    print("已传送完毕,下一步进行文件一致性比对")
                    if server_md5 == client_md51:
                        print("经过比对服务端与客户端下载的文件一致！！！")
                        sock.send(b'203')
                    else:
                        print("经过比对服务端与客户端下载的文件不一致！！！")
            else:
                print("服务器异常")
        elif action =="put":
            # 获取文件的大小
            data_fize = os.path.getsize(filename)
            # 获取文件的MD5值以便进行文件上传后一致性的校验
            obj = hashlib.md5(b'yanglongyue')  # 加盐
            with open(filename, 'rb') as f:
                for i in f:
                    obj.update(i)
                client_md5 = obj.hexdigest()
                print("client_md5:" + client_md5)
            data_dict = {'action': action, 'filename': filename, 'data_fize': data_fize, "client_md5": client_md5}

            # 转换成json字符串进行传递
            data_dict_json = json.dumps(data_dict)
            # 为了防止发生黏包，将data_dict_json的大小使用struct压包传到服务端，再传送数据过去
            data_dict_json_pack = struct.pack("i", len(data_dict_json))
            sock.send(data_dict_json_pack)
            sock.send(data_dict_json.encode('utf-8'))
            # 接收服务端返回的状态码
            code = sock.recv(1024).decode('utf-8')
            print(code)
            if code == '200':
                print("连接服务端成功，进行上传")
                with open(filename, 'rb') as f:
                    for i in f:
                        sock.send(i)
                code_md5 = sock.recv(1024).decode('utf-8')
                if code_md5 == "203":
                    print("文件经过比对完全一致！！！,客户端文件上传完毕！！！")
                else:
                    print("文件经过比对不一致！！！,客户端文件上传有缺失！！！")
            else:
                print("服务器异常")
    except Exception as e:
        print(e)