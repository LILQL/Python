q=[]
tmp=[]

l=0
r=len(q)
k=0

def merge_sort(q,l,r):
    mid =(l+r)/2
    merge_sort(q,l,mid),merge_sort(q,mid+1,r)
    i=l
    j=mid+1
    k=0
    while(i<=mid and j<=r):
        if(q[i]>q[j]):
            tmp[k]=q[i],i+1,k+1
        else:
            tmp[k]=q[j],j+1,k+1
    while(i<=mid):
        tmp[k]=q[i],i+1,k+1
    while(j<=r):
        tmp[k]=q[j],j+1,k+1

    for i,j in range(0,r):
        q[i]=tmp[j]

if __name__ == '__main__':
    n=int(input("number of count"))

for i in range(0,n):
    i=int(input())
    q.append(i)

merge_sort(q,0,r)

for i in range(0,n):
    print(q[i],end=" ")