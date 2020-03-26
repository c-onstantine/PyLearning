# 通过在定义类时  类名后面加小括号 加上继承的类
# 子类无法访问父类的私有属性
class Animal:
    def sleep(self):
        print("睡觉")

    def eat(self):
        print("吃饭")


class Dog(Animal):
    def yell(self):
        print("汪汪汪")
    def eat(self):
        print("狗吃粑粑")
        super().eat()



dog=Dog()
dog.sleep()
dog.eat()