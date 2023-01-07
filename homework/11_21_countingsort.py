import random

def counting_sort(q):
    maxV=max(q)        #取出最大值
    minV=min(q)        #取出最小值
    bucketlen=maxV -minV + 1
    bucket=[0]*bucketlen  #初始化桶
    sortIndex=0           #反装填的索引
    qlen=len(q)             
    for i in range(0,qlen):        
        bucket[q[i]-minV]+=1  #记录每一个数的出现次数 存在桶里

    for j in range(0,bucketlen): #反装填到原始数组
        while bucket[j]>0:  #标记的数字的出现次数
            q[sortIndex]=j+minV  #反装填
            sortIndex+=1
            bucket[j]-=1   #填一次减一次
    return 


if __name__=="__main__":

    q=[]    
    n=int(input("number of count:"))

    for i in range(0,n):
        i=random.randint(0,10000)
        q.append(i)

    for i in range(0,n):
        print("%d"%q[i],end=" ")

    counting_sort(q)

    print("\n")
    for i in range(0,n):
        print("%d"%q[i],end=" ")