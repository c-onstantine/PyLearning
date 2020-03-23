mylist=["1","2","3","4","1"]

# 统计列表长度
print(len(mylist))
# 统计列表中某个数据出现的次数
print(mylist.count("1"))
# 有多个数据时，删除第一个匹配的元素
mylist.remove("1")

print(mylist)