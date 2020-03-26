poem="风急天高猿啸哀，\t\n渚清沙白鸟飞回。\t\n无边落木萧萧下，\t\n不尽长江滚滚来。\t\n万里悲秋常作客，\t\n百年多病独登台。\t\n艰难苦恨繁霜鬓，\t\n潦倒新停浊酒杯。"

# 字符串分隔 默认空白字符分隔 可以指定分隔符
p_list=poem.split()
print(p_list)

s="---".join(p_list)
print(s)