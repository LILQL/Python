#测试错误出现点
#在错误日志中找到错位类型
'''
    print("-----b-----")
    f = open("re.txt","r")
    print("-----e-----")
'''
#捕获异常
'''
try:
    print("-----b-----")
    f = open("re.txt","r")
    print("-----e-----")
except IOError: #输入/输出异常
    pass      #程序执行且结束但非完全执行 e 没有被打印
'''
#多种异常处理
'''
try:
    print("-----b-----")
    f = open("re.txt","r")
    print("-----e-----")
    print(num)
except (NameError,IOError):
    print("错误")
'''
# as 获取错误描述
'''
try:
    print("-----b-----")
    print(num)
    f = open("re.txt","r")
    print("-----e-----")
    
except (NameError,IOError) as result:
    print("错误")
    print(result)
    #程序执行且结束,故第二种错误不会被处理
'''    
# Exception 为所有异常的父类

#try...finally和嵌套
#finally为最终都要执行的
#finally与try模块为局部模块，进行文件操作(变量为同一作用域)要进行嵌套
'''
try:
    print("-----b-----")
    f = open("test.txt","r")
    print("-----e-----")
    try:
        while True:
            content = f.readline()
            print(num)
    except NameError as result:
        print(result,end=" ")
        print("命名异常")
    finally:
        f.close()
        print("文件关闭")
except IOError: 
    pass  
'''