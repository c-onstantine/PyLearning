my_dic={"name":"fei"}
# 取值
# 取值时  如果指定的 key不存在 则报错
print(my_dic['name'])

# 增加/修改
my_dic['age']=18
# key存在 则会修改这个键值对的值
my_dic['name']="gg"

print(my_dic)


# 删除

my_dic.pop('name')

print(my_dic)