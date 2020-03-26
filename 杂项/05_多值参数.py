'''
参数名前增加一个*可以接收元组
参数名前增加两个*可以接收字典
'''

def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)

demo(1)
demo(1,2,3,4,5)
demo(1,2,3,4,5,name="xiaoming",age=18)

def demo2(*args,**kwargs):
    print(args)
    print(kwargs)

tp=(1,2,3)
dic={"name":"xiaoming","age":18}
demo2(*tp,**dic)