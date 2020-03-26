# 类中的方法 第一个参数必须是 self
# 创建对象：  对象=类名()

class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("汤姆爱喝水")

cat=Cat()
cat.eat()
cat.drink()