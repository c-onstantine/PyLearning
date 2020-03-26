'''
既不需要访问 实例属性 或者调用 实例方法
也不需要访问 类属性 或者调用 类方法
使用静态方法
'''
class A:
    count=0
    def __init__(self):
        A.count+=1

    @classmethod
    def Amethod(cls):
        print("当前类的实例个数%d" % cls.count)

    # 静态方法定义语法
    @staticmethod
    def run():
        print("跑步")

# 类名.静态方法名 不需要创建对象 
A.run()