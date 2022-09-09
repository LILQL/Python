# list中的元素可以互不相同，且可以进行嵌套，
# 如列表嵌套列表（类似于二维数组）
# -1为末尾的开始位置
# 可使用+进行拼接，*表示重复

# 增[append,extend,insert]
'''
namelist=[11,22,33]
for name in namelist:
    print(name)

nametemp =input("append:")
namelist.append(nametemp)
b= [1,3]
namelist.append(b)#普通追加
namelist.extend(b)#拆解追加
namelist.insert(1,3)#下标+元素的插入

for name in namelist:
    print(name)
'''

#删[del,pop(),remove()]
'''
namelist=['1','2','3','4',"test",5]
print("before")
for name in namelist:
    print(name)

del namelist[2]#在指定位置删除
namelist.pop()#弹出最后一个内容（出栈）
namelist.remove("test")#关键字删除，默认情况下，删除索引较小的相同关键字

print("\n")
print("after")
for name in namelist:
    print(name)
'''

#改
'''
namelist=['1','2','3','4',"test",5]
print("before")
for name in namelist:
    print(name)

namelist[0]=114514#指定目标即可

print("\n")
print("after")
for name in namelist:
    print(name)
'''
#查[in,not in,index,count]
'''
#查找是否存在
namelist=['1','2','3','4',"test",5]
findname=input("find:")
if findname in namelist:
    print("ture")
else:
    print("false")

print(namelist.index("3",0,6))#指定名字与范围，查找位置,符合左闭右开

print(namelist.count("3"))#统计元素的出现次数
'''

#排序
'''
a=[1,5,3,6,5,4,7]
a.reverse() #反转列表
a.sort()#升序排列
a.sort(reverse=True)#降序排列
'''

#嵌套列表操作(实例)
namelist=[1,2,3,4,5,6,7,8,9]
offices=[[],[],[]]
import random
for name in namelist:
    index1 = random.randint(0,2)
    offices[index1].append(name)

i=1
for office in offices:
    print("stdio_%d has %d person"%(i,len(office)))
    i+=1
    for name in office:
        print("names is:%d"%name)
    print("\n")
    print("-"*20)