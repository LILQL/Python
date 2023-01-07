list_1 = [1, 2, 3, 4]
count = 0
for a in list_1:
    for b in list_1:
        # print(a)
        for c in list_1:
            if (a != b) and (a != c) and (b != c):
                count += 1
                print(a, end="")
                print(b, end="")
                print(c, end=" ")

print("")
print("共计%d个结果" % count)


import math
import time
start = time.perf_counter()  #起始时间非常小 可以记做0
for n in range(-100,27956):
    x = int(math.sqrt(100+n))
    y = int(math.sqrt(100+168 + n))
    if 100+n ==x*x and 268+n == y*y :
        print(n)
end1 = time.perf_counter()  #结束的时间
time =end1 -start
print(time)


year = int(input('请输入年份:'))
month = int(input('请输入月份:'))
day = int(input('请输入日期:'))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month -1]
    sum+=day
else:
    print ('您输入的日期超出范围！！')

leap = 0
if (year % 400 == 0) or ((year %4==0) and (year % 100 !=0)):
    leap=1
if (leap == 1) and (month > 2):
    sum += 1
print ('今天是今年的第%s天.' % sum)