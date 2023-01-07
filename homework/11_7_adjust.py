import timeit
import random

def adjust(arr,l,r):
    if(l<r):
        i=l
        j=r
        x=arr[l] #基数
        while(i<j):
            while(i<j and arr[j]>=x):
                j=j-1
            if(i<j):
                arr[i]=arr[j]
            while(i<j and arr[i]<x):
                i=i+1
            if(i<j):
                arr[j]=arr[i]
    
        arr[i]=x
        #i作为基数不被调用，故递归时被排除
        adjust(arr,l,i-1)
        adjust(arr,i+1,r)



if __name__ =="__main__":

    arr=[]

    s=int(input("the count of numbers:"))

    for i in range(0,s):
        i=random.randint(0,10000)
        arr.append(i)
        

    l=0
    r=len(arr)-1 #注意数组越界问题

    for i in range(0,r):
        print("%d"%arr[i],end=" ")

    aa=timeit.default_timer() #start

    adjust(arr,l,r)

    bb=timeit.default_timer() #end

    print("\n")
    for i in range(0,r):
        print("%d"%arr[i],end=" ")

    print('\nRunning time: %s Seconds'%(bb-aa))