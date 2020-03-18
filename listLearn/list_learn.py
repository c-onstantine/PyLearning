mylist=["1","2","3","4"]

#索引取值
print(mylist[1])

# 根据内容获取索引

print(mylist.index("1"))

# 修改
# 超出index会报错
mylist[2]="二"

# 增加  向列表末尾追加数据
mylist.append("5")
# 在指定位置插入数据
mylist.insert(1,"1.1")
# 把另一个列表追加到当前列表末尾
newlist=['a','b','c']
mylist.extend(newlist)


print(mylist)