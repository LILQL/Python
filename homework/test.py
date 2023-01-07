def getMoney(number,money):#取款函数
        if isinstance(number,(int,float))==True:
            if number>=0 and number<=money:
                print("转入%.1f元"%number,end=" ")
                money=money-number
                print("余额为%.1f元"%money)
            else:
                print("余额不足！")
        else:
            print("取款金额应该为数字类型！")

def putMoney(number,money):#存款函数
        if isinstance(number,(int,float))==True:
            if number>=0:
                money=money+number
                print("转入%.1f元"%number,end=" ")
                print("余额为%.1f元"%money)
            else:
                print("存款金额不能为负数！")
        else:
            print("存款金额应该为数字类型！")


if __name__=='__main__':
        while True:
            money=1000
            opNum = int(input('''菜单\n    0：退出\n    1：存款\n    2：取款\n'''))
            if opNum == 1:
                number = int(input("请输入存款金额："))
                putMoney(number,money)
            elif opNum==2:
                number=int(input("请输入取款金额："))
                getMoney(number,money)
            elif opNum==0:
                print("您已退出系统\n")
                break
            else:
                print("请输入有效操作！")