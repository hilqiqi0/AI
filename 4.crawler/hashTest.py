# -*- coding: utf-8 -*-

# HASH算法（对某段信息打指纹，能够压缩信息，
#HASH算法是不可逆的）：

import hashlib
# HASH某个字符串
def hashStr(strInfo):
    h = hashlib.sha256()
    h.update(strInfo.encode("utf-8"))
    return h.hexdigest()

# HASH文件
chunkSize = 4096 # 每次读取文件的字节数
def hashFile(fileName):
    """
    对文件做hash
    """
    h = hashlib.sha256()
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(chunkSize)
            if not chunk:#当读文件到结尾处时，跳出循环
                break
            h.update(chunk)
    return h.hexdigest() # 得到文件最终的hash值

if __name__ == "__main__":
    print(hashStr("hello world"))
    print(hashStr("hello world1"))
    
    print(hashFile("test.txt"))
    


