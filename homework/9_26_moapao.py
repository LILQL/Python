import timeit

arr=[]

s=int(input("the count of numbers:"))

for i in range(0,s):
    i=int(input("number:"))
    arr.append(i)

for i in arr:
    print(i,end=" ")

print("\n")
print("-"*20)

bj=len(arr)-1 #优化2：最后一次的变化位置，即一轮交换的末尾，忽略后面的有序部分

fl=0 #优化2：记录每一次变化的位置，其目的是得到最后一次变化的位置

jg=True #优化1：设置特判点，目地是为了在一轮交换完成后判断是否发生交换:

aa=timeit.default_timer() #start

for i in range(0,len(arr)-1):
    for j in range(0,bj):
        if(arr[j]>arr[j+1]):
            jg=False #若有交换则变为False，否则为True
            print("交换%d与%d"%(arr[j],arr[j+1]))
            arr[j],arr[j+1]=arr[j+1],arr[j]
            fl=j 
    
    bj=fl

    if(jg): #优化1：特判，值为True则无交换，说明有序，直接跳出循环
        print("break")
        break

bb=timeit.default_timer()#end

for i in arr:
    print(i,end=" ")

print('\nRunning time: %s Seconds'%(bb-aa))