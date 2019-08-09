import re

s =  "alex:1994,sunny:1993"

pattern = r"\w+:\d+"

# re模块调用findall
l = re.findall(pattern,s)
print(l)

pattern = r"(\w+):\d+"

# re模块调用findall
l = re.findall(pattern,s)
print(l)

pattern = r"(\w+):(\d+)"

# re模块调用findall
l = re.findall(pattern,s)
print(l)

pattern = r"\w+:\d+"
# 使用compile调用
regex = re.compile(pattern)
l = regex.findall(s)
print(l)


# 按照匹配的内容切割字符串
l = re.split(r":|,",s)
print(l)

# 替换匹配的内容 ， 正则表达式，替换的字符串，目标字符串 （s）此处为s
s = re.sub(r"\s+",".","l love you baby",8)
print(s)

# 替换匹配的内容,结果同sub ,不同的是subn返回值提示替换了多少处内容
s = re.subn(r"\s+",".","l love you baby",8)
print(s)

