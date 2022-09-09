#1.tuple与list类似，但tuple元素无法修改，逗号隔开
#2.元素不可变，但嵌套元素可以改变
#3.只有一个元素时也要使用逗号隔开
'''
tup1=(50)
print(type(tup1)) #int
tup2=(50,)
print(type(tup2)) #tuple
tup3=(50,60,70)
print(type(tup3)) #tuple
'''
'''
tup_t=(1,2,3,4,5)
tup_t[-1]
tup_t[1:10] #即使超过元组边界,不会报错,自动停止
'''

#增
'''
tup1 =(12,34,56)

tup2 =("abc","xyz")

tup=tup1+tup2 #重开元组
print(tup)
'''

#删
'''
tup1 =(12,34,56)
del tup1
print(tup1) #报错,删除整个变量tup1
'''
#改
'''
tup1 =(12,34,56)

tup1[0]=100 #报错
'''


#查
