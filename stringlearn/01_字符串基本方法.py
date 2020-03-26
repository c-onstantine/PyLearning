s=" "
print(s.isspace())

# 判断数字

num_str="\u00b3"
print(num_str)
# 三个函数都是判断字符串中 是否包含数字  且从上到下 判断的范围越来越大
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())