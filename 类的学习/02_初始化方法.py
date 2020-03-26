# 创建对象会自动调用 init方法
class Cat:
    def __init__(self):
        print("初始化方法")

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("汤姆爱喝水")



cat=Cat()