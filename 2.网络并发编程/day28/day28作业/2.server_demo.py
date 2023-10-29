#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/2/14 14:16
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : 2.server_demo.py
@Software: PyCharm

'''

"""
利用socketserver ThreadingTCPServer实现多线程上传下载
"""
import socketserver
import struct
import json
import hashlib
import os


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        """
        此处写业务逻辑
        :return:
        pass
        """
        try:
            while True:
                data = self.request.recv(4)
                if data == "exit":
                    break
                # 先获取客户端传来的pack压缩包然后进行unpack解压
                data_json_unpack = struct.unpack("i", data)[0]
                print(data_json_unpack)
                # 根据unpack获取的元组中的数字长度，再去内存缓冲区取data_json_unpack长度的数据，即客户端第二次send过来的json字符串
                data_json_unpack_recv = self.request.recv(data_json_unpack)
                file_info = json.loads(data_json_unpack_recv)
                print('file_info', file_info)

                # 进行接收处理客户端上传的文件
                action = file_info.get('action')
                filename = file_info.get('filename')
                print(action, filename)
                if action == "put":
                    # 返回客户端状态码代表接收成功
                    self.request.send(b'200')
                    # 进行接收处理客户端上传的文件
                    data_fize = file_info.get('data_fize')
                    client_md5 = file_info.get('client_md5')
                    print(action, filename, data_fize, client_md5)
                    obj = hashlib.md5(b'yanglongyue')
                    with open("put/" + filename, 'wb') as f:
                        data_fize_len = 0
                        while data_fize_len < data_fize:
                            data_len = self.request.recv(1024)
                            data_fize_len += len(data_len)
                            f.write(data_len)
                            obj.update(data_len)
                            print("总大小%s,已上传%s" % (data_fize, data_fize_len))
                        server_md5 = obj.hexdigest()
                        print(server_md5)
                        print("已传送完毕,下一步进行文件一致性比对")
                        if server_md5 == client_md5:
                            print("文件经过比对完全一致！！！")
                            self.request.send(b'203')
                        else:
                            print("经过比对服务端与客户端上传的文件不一致！！！")
                elif action == "get":
                    # 返回客户端状态码代表接收成功
                    self.request.send(b'201')
                    # 获取文件的大小
                    data_fize = os.path.getsize(filename)
                    print(data_fize)
                    # 获取文件的MD5值以便进行文件上传后一致性的校验
                    obj = hashlib.md5(b'yanglongyue')  # 加盐
                    with open(filename, 'rb') as f:
                        for i in f:
                            obj.update(i)
                        client_md5 = obj.hexdigest()
                        print("client_md5:" + client_md5)
                    data_dict = {'action': action, 'filename': filename, 'data_fize': data_fize,
                                 "client_md5": client_md5}

                    # 转换成json字符串进行传递
                    data_dict_json = json.dumps(data_dict)
                    print(data_dict_json)
                    # 为了防止发生黏包，将data_dict_json的大小使用struct压包传到服务端，再传送数据过去
                    data_dict_json_pack = struct.pack("i", len(data_dict_json))
                    self.request.send(data_dict_json_pack)
                    self.request.send(data_dict_json.encode('utf-8'))
                    with open(filename, 'rb') as f:
                        for i in f:
                            self.request.send(i)
                    code_md5 = self.request.recv(1024).decode('utf-8')
                    if code_md5 == "203":
                        print("文件经过比对完全一致！！！,客户端文件下载完毕！！！")
                    else:
                        print("文件经过比对不一致！！！,客户端文件下载有缺失！！！")

                else:
                    print("请正确输入命令参数")
        except Exception as e:
            print(e)
        finally:
            self.request.close()


# 创建socket对象
server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)

server.serve_forever()
