# -*- coding: utf-8 -*-

import base64
import json

# 加密函數
def encode_base64(data):
    # 將字典轉換成json字串
    json_str = json.dumps(data)
    # 將json字串編碼成bytes，然後用base64加密
    bytes_encoded = base64.b64encode(json_str.encode('utf-8'))
    return bytes_encoded.decode('utf-8')

# 解密函數
def decode_base64(encoded_str):
    # 將加密過的字串解碼成bytes，然後用base64解密
    bytes_decoded = base64.b64decode(encoded_str)
    # 將bytes轉換成json字串，然後將json字串轉換成字典
    data = json.loads(bytes_decoded.decode('utf-8'))
    return data

# 示範數據
original_data = {
  "xxxx": "xxxx",
  "xxx": "xxxx"
}


# 加密
encoded_data = encode_base64(original_data)
print("encode_base64:", encoded_data)

# 解密
decoded_data = decode_base64(encoded_data)
print("decode_base64:", decoded_data)
