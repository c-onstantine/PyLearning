# 使用类名.属性名调用 类属性 不要使用对象名.属性名 虽然这样取值没有问题 但是修改值 会在对象中创建这样一个属性 无法修改类属性的值
# 类方法需要用修饰器@classmethod 来标识，告诉解释器这是一个类方法
# 类方法的第1个参数应该是cls
class A:
    count=0
    def __init__(self):
        A.count+=1

    @classmethod
    def Amethod(cls):
        print("当前类的实例个数%d" % cls.count)


a=A()
b=A()
c=A()
print(A.count)
print(c.count)
A.Amethod()