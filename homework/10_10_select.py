import timeit

arr=[]

s=int(input("the count of numbers:"))

for i in range(0,s):
    i=int(input("number:"))
    arr.append(i)

for i in arr:
    print(i,end=" ")

print("\n")

aa=timeit.default_timer() #start

for i in range(0,len(arr)-1):
    flagmid=i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[flagmid]):
            flagmid=j
    
    if(i!=flagmid):
        arr[i],arr[flagmid]=arr[flagmid],arr[i]

bb=timeit.default_timer()#end


for i in arr:
    print(i,end=" ")

print('\nRunning time: %s Seconds'%(bb-aa))