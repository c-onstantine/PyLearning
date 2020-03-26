# 如果不同的父类中存在同名的方法，子类对象在调用方法时，会调用哪一个父类中的方法呢?
'''
提示:开发时，应该尽量避免这种容易产生混淆的情况! --如果父类之间存在同名
的属性或者方法，应该尽量避免使用多继承

如果有相同的方法 那么会先调用 先继承的类的 方法
'''
class A:
    def demoa(self):
        print("a方法")

class B:
    def demob(self):
        print("b方法")

class C(A,B):
    def democ(self):
        print("cde fangfa")

c=C()
c.demoa()