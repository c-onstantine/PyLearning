'''
1.创建一个Exception 的对象
2.使用raise关键字抛出异常对象

'''

def get_passwd():
    passwd=input("请输入密码：")

    l=len(passwd)

    if l>=8:
        return passwd

    ex=Exception("密码长度必须大于等于8位")
    raise ex
try:

    get_passwd()
except Exception as result:
    print(result)