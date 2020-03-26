my_dic={"name":"fei","age":18}

# 统计键值对数量
print(len(my_dic))

# 合并字典 update
tem_dic={"height":1.85}
# 如果字典中有相同的key  则新值覆盖旧值
my_dic.update(tem_dic)


print(my_dic)