num=10
# 全局变量建议 定义在所有函数的上方，  
def demo1():
    global num
    num=99
    print("函数1："+str(num))

def demo2():
    print("函数2："+str(num))


demo1()
demo2()