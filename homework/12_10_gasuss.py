import timeit

def normal(max):
    sum=0
    for i in range(1,max+1):
        sum=sum+i
    return sum

def gasuss(max):
    sum=0
    sum=(1+max)/2*max  

    return sum


if __name__ == '__main__':
    t=int(input())

    aa=timeit.default_timer() #start
    print("normal:%d"%normal(t),end="\n")
    bb=timeit.default_timer()#end
    nor=bb-aa

    print("time:%f"%nor)


    cc=timeit.default_timer() #start
    print("gasuss:%.1f"%gasuss(t))
    dd=timeit.default_timer()#end
    gas=dd-cc

    print("time:%f"%gas)