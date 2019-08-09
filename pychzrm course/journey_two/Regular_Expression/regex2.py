import re

pattern = r"(ab)cd(?P<hfk>ef)"
regxt = re.compile(pattern)
obj = regxt.search("abcdefghi") # match 对象

#                           属性变量
# pos 匹配的目标字符串开始位置
print(obj.pos)
# endpos 匹配的目标字符串结束位置
print(obj.endpos)
# re 正则表达式
print(obj.re)
# string 目标字符串
print(obj.string)
# lastgroup 最后一组的名称
print(obj.lastgroup)
# lastindex 最后一组的序号
print(obj.lastindex)

#                              属性方法
# span() 获取匹配内容的起止位置
print(obj.span())
# start() 获取匹配内容的开始位置
print(obj.start())
# end() 获取匹配内容的结束位置
print(obj.end())
# groupdict() 获取捕获组字典,组名为键,对应内容为值
print(obj.groupdict())
# groups() 获取子组对应内容
print(obj.groups())
# group(n = 0) 获取match对象匹配内容
print(obj.group())

