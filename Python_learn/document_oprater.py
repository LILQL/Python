#打开与关闭
'''
f = open("test.txt","w")# w 写入，存在会覆盖，不存在则新建
                        # rb 二进制读取
                        # r 只读（默认）
f.write("hello I'am here")                    
f.close()
'''
#读[read,readline,readlines]
#read 读取指定字符数，开始定位在头部，可设置读取个数
'''
f = open("test.txt","r")

content_t = f.read(5)

print(content_t)

f.close()
'''
#readlines 读取行数为列表
'''
f = open("test.txt","r")
conetnt_t = f.readlines()
print(conetnt_t)
f.close
'''

#os
import os
os.rename("test.txt","1.txt")
os.remove("1.txt")
os.mkdir("name")
os.rmdir("name")
os.getcwd() #获取当前目录
os.chdir("../") #改变文件夹目录（位置）
os.listdir("./") #遍历当前目录
