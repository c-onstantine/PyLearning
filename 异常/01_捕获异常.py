'''
可能出现的错误
ZeroDivisionError
ValueError
'''
try:
    num=int(input("请输入一个数字:\t\n"))

    result=8/num

    print(result)
except ZeroDivisionError:
    print("0不能做除数")
except ValueError:
    print("请输入整数")
else:
    print("没有异常才执行")
finally:
    print("无论是否有异常都执行")


print("-"*50)