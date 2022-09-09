#含参
'''
def add_number(a,b):
    c = a+b
    print(c)

add_number(23,43)
'''

#返回值
'''
def add_number(a,b):
    return a+b

result_1=add_number(23,43)
print(result_1)
'''

#多个返回值
'''
def divid(a,b):
    shang = a//b
    yvshu = a%b
    return shang,yvshu

sh,yv = divid(5,2)

print(sh,yv)
'''

#练习
'''
def line():
    print("-"*30)

def many_line(a):
    for i in range(0,a+1):
        line()

u=int(input())


many_line(u)
'''

#全局变量与局部变量
#局部中的全局使用
'''
global a
'''


