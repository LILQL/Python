import random


def max_heapify(arr,start,end):
    dad=start
    son=dad*2+1
    while(son<=end):
        if(son+1<end and arr[son]<arr[son+1]):
            son=son+1
        if(arr[dad]>arr[son]):
            return
        else:
            arr[dad],arr[son]=arr[son],arr[dad]
            dad=son
            son=dad*2+1

def heap_sort(arr,len):
    i=int(len/2-1)+1
    while(i>0):
        max_heapify(arr,i,len-1)
        i=i-1
    
    i=len-1
    while(i>0):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,0,i-1)
        i=i-1




if __name__ == '__main__':

    q=[]


    n=int(input("number of count:"))

    for i in range(0,n):
        i=random.randint(0,10000)
        q.append(i)
    
    for i in range(0,n):
        print(q[i],end=" ")

    heap_sort(q,len(q))
    
    print("\n")

    for i in range(0,n):
        print(q[i],end=" ")