num_list=[1,2,3,4,5,6]


# else 中的内容只有当for循环遍历完成 不是通过break 跳出时  才会执行
for i in num_list:
    print(str(i)+" ")
    if i == 3:
        break
else:
    print("遍历完成")