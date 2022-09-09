#1.键值对（key-value）集合,无序，查找速度极快
#2.键（key）必须使用不可变类型
#3.同一个字典中，key必须唯一，即不重复
#4.理解为下标变为了key

#定义
'''
info ={"name":"abc","age":18}
#访问
print(info["name"])
'''
#访问了不存在的键（错误捕捉）
'''
#print(info["gender"]) #直接访问，报错

print(info.get("gender")) #使用get，没找到会返回None（错误捕捉）

print(info.get("gender","m"))#自定义抛出结果
'''

#增
'''
info ={"name":"abc","age":18}
newID= input("学号：")
info["id"]=newID
'''

#删(del,clear)
#[del] 删除
'''
info ={"name":"abc","age":18}

del info["name"] #键值对删除
del info #字典删除
'''
#[clear] 清空
'''

info ={"name":"abc","age":18}

#info["age"].clear #键值对清空，报错
info.clear() #dict完全清空
'''

#改
'''
info ={"name":"abc","age":18}

info["name"]="qianli"
'''

#查
'''
info ={"name":"abc","age":18}
print(info.keys()) #所以的键
print(info.values())#所以的值
print(info.items())#所有的项，获取格式为tuple

for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''
#列表下标的提取
'''
list_2=[1,2,3,4]

for i,x in enumerate(list_2):
    print(i+1,x)
'''



