"""
flags 扩展功能展示
"""

import re
s = """Hello
河北
"""
# 生成正则表达式对象
regex = re.compile(r"\w+")
# 根据正则表达式匹配目标字符串内容
l = regex.findall(s)
print(l)

# 生成正则表达式对象 A == ASCII 元字符只能匹配ascii码
regex2 = re.compile(r"\w+",flags=re.A)
# A == ASCII 元字符只能匹配ascii码 不能识别汉字
a = regex2.findall(s)
print(a)

# 不区分大小写
regex3 = re.compile(r"[a-z]]+",flags=re.I)
i = regex3.findall(s)
print(i)

# S == DOTALL 使 . 可以匹配换行
regex4 =re.compile(r".+",flags=re.S)
s= regex4.findall(s)
print(s)

# M == MULTILINE 使 ^ $可以匹配每一行的开头结尾位置
regex5 = re.compile(r"Hello$",flags=re.M)
m = regex5.findall(s)
print(m)


# X == VERBOSE 为正则添加注释
pattern = """
\w # Hello
\+ # 河北
"""
regex6 = re.compile(pattern,flags=re.X)
x = regex6.findall(s)
print(x)