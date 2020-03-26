'''
open函数默认是 只读方式
'''
file =open("./text.txt","a",encoding="utf-8")

file.write("\t\n-----林嗣环《口技》")

file.close()