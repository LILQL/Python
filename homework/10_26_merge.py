import random

def merge_sort(list1):
    if len(list1) <= 1:
        return
    mid = len(list1) // 2
    L = list1[:mid]
    R = list1[mid:]
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            list1[k] = L[i]
            i += 1
        else:
            list1[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        list1[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        list1[k] = R[j]
        k += 1
        j += 1

if __name__ == '__main__':

    q=[]


    n=int(input("number of count:"))

    for i in range(0,n):
        i=random.randint(0,10000)
        q.append(i)
    
    for i in range(0,n):
        print(q[i],end=" ")

    tmp=merge_sort(q)
    
    print("\n")
    for i in range(0,n):
        print(q[i],end=" ")



