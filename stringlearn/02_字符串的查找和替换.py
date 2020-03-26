hello_str="hello world"

# 判断以某个字符串开始
print(hello_str.startswith("hello"))

# 判断以某个字符串结束
print(hello_str.endswith("rld"))

# 查找指定字符串
# index 同样也可以查找
print(hello_str.find("llo"))

# index 与 find 的 区别是 find查找不存在的 字符串会返回-1 index 会报错
print(hello_str.find("abd"))
#替换字符串
# replace 执行后 会返回新的字符串 不会修改原有字符串内容
print(hello_str.replace("world","python"))

print(hello_str)