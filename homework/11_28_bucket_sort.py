import random

def counting_sort(q):
    maxV=max(q)        #取出最大值
    minV=min(q)        #取出最小值
    bucket_num=(maxV-minV)//5 + 1
    buckets = [[] for _ in range(int(bucket_num))] #初始化（列表嵌套）
    sortIndex=0           #反装填的索引
    qlen=len(q)             
    for i in range(0,qlen):        
        buckets[int((q[i]-minV)//5)].append(q[i])   #把数放入对应的桶
                                                    #计数排序开了n个桶
    for i in buckets:
        for j in sorted(i):      #桶内排序
            q[sortIndex]=j
            sortIndex+=1
    
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