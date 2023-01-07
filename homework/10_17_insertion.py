import timeit
import random

arr=[]

s=int(input("the count of numbers:"))

for i in range(0,s):
    i=random.randint(0,10000)
    arr.append(i)

for i in arr:
    print(i,end=" ")

print("\n")

aa=timeit.default_timer() #start

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while(j >= 0 and key<arr[j]):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key

bb=timeit.default_timer()#end


for i in arr:
    print(i,end=" ")

print('\nRunning time: %s Seconds'%(bb-aa))


