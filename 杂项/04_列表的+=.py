# 列表的+= 在函数中使用+=操作全局变量 相当于调用 extend方法，会改变全局变量  但是 列表相加 不会

my_list=[1,2,3]

def demo1(ml):
    ml=ml+ml
    print(ml)


demo1(my_list)
print(my_list)