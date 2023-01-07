import timeit
import random

arr=[]

s=int(input("the count of numbers:"))

for i in range(0,s):
    i=random.randint(0,10000)
    arr.append(i)

n=len(arr)
gap=int(n/2)

for i in arr:
    print(i,end=" ")

print("\n")

aa=timeit.default_timer() #start

while(gap>0):
    for i in range(gap,len(arr)):
        key=arr[i]
        j=i-gap
        while(j >= 0 and key<arr[j]):
            arr[j+gap]=arr[j]
            j-=gap
        arr[j+gap]=key
    gap=int(gap/2)

bb=timeit.default_timer()#end


for i in arr:
    print(i,end=" ")

print('\nRunning time: %s Seconds'%(bb-aa))
