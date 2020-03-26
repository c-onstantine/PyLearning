# 在定义属性或方法时，在属性名或者方法名前增加两个下划线，定义的就是私有属性或方法
# python 中并没有绝对的 私有 是伪私有
class Cat:
    def __init__(self):
        self.__age=5
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("汤姆爱喝水")
    def get_age(self):
        print("小猫的年龄是%s岁" % self.__age)


cat=Cat()
cat.get_age()
# python对私有属性的处理 是  _类名__私有属性名  通过这样可以访问私有属性和方法 但是这是不提倡的 
print(cat._Cat__age)

