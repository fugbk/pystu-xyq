# encoding = utf-8
__author__ = "Ang Li"

import json
import struct

header_dic = {
    "file_name": "xxxx",
    "md5": 22222222222222222,
    "total_size": 12132
}
header_json = json.dumps(header_dic)
header_bytes = header_json.encode('utf-8')
print(type(header_bytes))

header_size = len(header_bytes)
print(type(header_size))
print("报文头部长度：", header_size)

# 第二步：发送报文头部

obj = struct.pack('i', header_size)
print(type(obj))
 
