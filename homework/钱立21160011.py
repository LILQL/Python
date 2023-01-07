import time
import random
def calculation_time(t1,t2):
    t3 = t2-t1
    return t3
#冒泡算法
def bubble_sort(array):
    bj=len(array)-1 #优化2：最后一次的变化位置，即一轮交换的末尾，忽略后面的有序部分

    fl=0 #优化2：记录每一次变化的位置，其目的是得到最后一次变化的位置

    jg=True #优化1：设置特判点，目地是为了在一轮交换完成后判断是否发生交换:

    for i in range(0,len(array)-1):
        for j in range(0,bj):
            if(array[j]>array[j+1]):
                jg=False #若有交换则变为False，否则为True
                array[j],array[j+1]=array[j+1],array[j]
                fl=j 
    
        bj=fl

        if(jg): #优化1：特判，值为True则无交换，说明有序，直接跳出循环
            print("break")
            break

    return array
#选择排序
def choose_sort1(array):
    for i in range(0,len(array)-1):
        flagmid=i
        for j in range(i+1,len(array)):
            if(array[j]<array[flagmid]):
                flagmid=j
    
        if(i!=flagmid):
            array[i],array[flagmid]=array[flagmid],array[i]

    return array

#插入排序
def insertion_sort(ls):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while(j >= 0 and key<array[j]):
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return ls

#希尔排序
def shell_sort(a_list):
    n = len(a_list)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i - gap >= 0:
                if a_list[i] < a_list[i - gap]:
                    a_list[i], a_list[i - gap] = a_list[i - gap], a_list[i]
                    i -= gap
                else:
                    break
        #print(a_list)
        gap //= 2
    return a_list
#归并排序
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


#快速排序
def quick_sort(b, low, high):
    if low >= high:
        return b
    i = low
    j = high
    pivot = b[low]
    while i < j:
        while i < j and b[j] > pivot:
            j -= 1
        b[i] = b[j]
        while i< j and b[i] < pivot:
            i += 1
        b[j] = b[i]
        # print(a)
    b[j] = pivot
    quick_sort(b, low, j - 1)
    quick_sort(b, j + 1, high)
    return b
#堆排序
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[i]
    while j <= high:
        if j < high and li[j] < li[j + 1]:
            j = j + 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)
    return li


if __name__ == '__main__':
    x = int(input("数组的大小："))
    array = list(range(x))
    random.shuffle(array)
    print('排序前的数组',array)
    print('冒泡排序')
    t1 = time.time()
    print(bubble_sort(array))
    t2 = time.time()
    print('冒泡排序时间：',calculation_time(t1,t2))
    print('快速排序')
    t1 = time.time()
    print(array)
    t2 = time.time()
    print('快速排序时间：', calculation_time(t1, t2))
    print('选择排序')
    t1 = time.time()
    print(choose_sort1(array))
    t2 = time.time()
    print('选择排序时间：', calculation_time(t1, t2))
    print('希尔排序')
    t1 = time.time()
    print(shell_sort(array))
    t2 = time.time()
    print('希尔排序时间：', calculation_time(t1, t2))
    print('插入排序')
    t1 = time.time()
    print(insertion_sort(array))
    t2 = time.time()
    print('插入排序时间：', calculation_time(t1, t2))
    print('归并排序')
    t1 = time.time()
    print(merge_sort(array))
    t2 = time.time()
    print('归并排序时间：', calculation_time(t1, t2))
    print('堆排序')
    t1 = time.time()
    print(heap_sort(array))
    t2 = time.time()
    print('堆排序时间：', calculation_time(t1, t2))