n=int(input("wow:"))

res=[0]

a=[]

for i in range(0,n):
    t=int(input("down:"))
    a[i]=t
    res[i+1]=res[i]+a[i]