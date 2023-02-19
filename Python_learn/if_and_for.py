#if语句

'''
if False:
    print("True")
else:
    print("False")
'''
#随机数
'''
import random
x = random.randint(0,2)
print(x)
'''
#for语句
'''
for i in range(5):
    print(i)
'''
#从1-10的范围，步进值为-3
'''
for i in range(11,1,-3):
    print(i)
'''
#提取字符
'''
name = "chengdu"

for x in name:
    print(x,end="\t")
'''
#列表遍历
'''
a=["aa","bb"]
for i in range(len(a)):
    print(i,a[i])
'''
#或
'''
for name in a:
    print(name)
'''
#while语句
'''
i=0
while i<5 :
    print("第%d次循环"%(i+1))
    print("i=%d"%i)
    i+=1
'''
#while...else
#只要执行else,即使后续元素while条件仍然满足，程序结束
'''
count =-5
while (count!=0 and count<5):
    print(count,"小于5")
    count +=1
else:
    print(count,"大于或等于5")
'''
#1-100求和

'''
i=1
sum=0
while i<=100 :
    sum+=i
    i+=1
print(sum,end="\n")

i=1
sum=0
for i in range(1,101,1):
    sum+=i
print(sum)
'''
