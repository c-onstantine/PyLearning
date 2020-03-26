# python 实现单例 需要重写 __new__方法
class A:
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance
    def __init__(self):
        print("初始化")


    def play(self):
        print("播放music")


a=A()
print(a)
b=A()
print(b)
