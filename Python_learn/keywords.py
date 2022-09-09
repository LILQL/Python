#pass站位语句
'''
i=0
while i<10:
    i=i+1
    pass
    print("-"*30)
    if i==5:
        continue
    if i==10:
        break
    print(i)
'''
#break作用范围测试
for i in range(1,11,1):
    for j in range(1,11,1):
        if(i==5): 
            break
        print("*",end=" ")
    print("\n")
#作用范围为跳出一层循环