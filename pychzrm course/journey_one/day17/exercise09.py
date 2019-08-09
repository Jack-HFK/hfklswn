# 练习:参照下列代码现象,自定义生成器函数my_zip.
# list01 = ["张无忌","赵敏","周芷若"]
# list02 = [101,102,103]
# for item in zip(list01,list02):
#   print(item)

def my_zip(list01,list02):
  for i in range(len(list01)):
    yield (list01[i] ,list02[i])

for item in my_zip([2,4,45],[5,6,8]):
  print(item)

list01 = ["张无忌","赵敏","周芷若"]
list02 = [101,102]
for item in zip(list01,list02,list02):
  print(item)