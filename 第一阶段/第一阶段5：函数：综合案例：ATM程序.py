#定义全局变量
money = 5000000
name = None

#要求客户输入姓名
name = input("please input your name:")

#定义查询余额函数
def check_remain(shower_header):
    if money >= 0:
        if shower_header:
         print("---------Check remain money-------")
        print(f"Hello,{name}, your remain money is:{money}yuan\n")
    else:print("withdraw money is failed, there are not enough money")

#定义存款函数
def save_money(num):
    global money #money在函数内部定义为全局变量
    money = money+num
    print("---------Save money-------")
    print(f"Hello,{name}, Your save money is finished")
    print(f"Now,your save money in your account :{num}yuan")
    # 调用check_money函数查询余额
    check_remain(False)

#定义取款函数
def withdraw_money(num):
    global money
    money = money-num
    if money >= 0:
        print("Hello,sir, Your withdraw money is finished")
        print(f"Now,your withdraw money in your account :{num}yuan")
    else:
        print("withdraw money is failed, there are not enough money")

    #调用check_money函数查询余额
    check_remain(False)

#定义主菜单函数
def main():
    print("--------main menu--------")
    print(f"welcome to ATM of bank ,{name},please choose operation:")
    print("check remain please \t【input 1】")
    print("save money please \t\t【input 2】")    #通过\t制表符对其输出
    print("withdraw money please \t【input 3】")
    print("exit please \t\t\t【input 4】")
    return int(input("Please input your choose:"))

#设置无限循环保证程序不会退出
while True:
    keyborad_input = main()
    if keyborad_input == 1:
        check_remain(True)
        continue #通过continue继续下一次循环，一进来就回到了主菜单
    elif keyborad_input == 2:
        num=int(input("Please input how much money do you want to save:")) #把输入的字符串转换成数字
        save_money(num)
        continue
    elif keyborad_input == 3:
        num = int(input("Please input how much money do you want to withdraw:"))  # 把输入的字符串转换成数字
        withdraw_money(num)
        continue
    else:
        print("Programming exit")
        break   #通过break退出循环


