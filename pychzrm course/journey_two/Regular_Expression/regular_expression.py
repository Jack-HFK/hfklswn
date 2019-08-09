import re

k = "swn,小女子不才，未得公子青睐，88,66,公子向北走，小女子向南瞧，hfk"

s = re.findall("公子|小女子", k)
print(s)  # ['小女子', '公子', '公子', '小女子']

s = re.findall("小.子", k)
print(s)  # ['小女子', '小女子']

s = re.findall("[女子]", k)
print(s)  # ['女', '子', '子', '子', '女', '子']

s = re.findall("[a-z0-9]", k)
print(s)  # ['s', 'w', 'n', '8', '8', '6', '6', 'h', 'f', 'k']

s = re.findall("[^a-z0-9]", k)
print(
    s)  # [',', '小', '女', '子', '不', '才', '，', '未', '得', '公', '子', '青', '睐', '，', ',', ',', '公', '子', '向', '北', '走', '，', '小', '女', '子', '向', '南', '瞧', '，']

k = "swn,小女子不才,未得公子青睐,88,66,公子向北走,小女子向南瞧,hfk"

s = re.findall("^sw", k)
print(s)  # ['sw']

s = re.findall("fk$", k)
print(s)  # ['fk']

s = re.findall("^hfklswn$", "hfklswn")
print(s)  # ['hfklswn']

s = re.findall("公子*", k)  # 0个或多个
print(s)        # ['公子', '公子']

for i in k:
    s = re.findall("^[0-9a-z][a-z0-9]*$",i)
    print(s)

s = re.findall("[a-z]+",k)
print(s)        # ['swn', 'hfk']
s = re.findall("[a-z]*",k)
print(s)

k = "swn,小女子不才,未得公子青睐,888,666,公子向北走,小女子向南瞧,hfk"
s = re.findall("女子?",k)
print(s)    #  ['女子', '女子']

s = re.findall("8{3}",k)
print(s) # ['888']

s = re.findall("1[0-9]{10}","15685546654")
print(s)  # ['15685546654']

s = re.findall("8{4}","8,88,888,8888,88888")
print(s)   # ['8888', '8888']

s= re.findall("\d",k)
print(s) # ['8', '8', '8', '6', '6', '6']
s = re.findall("\D",k)
print(s)   # ['s', 'w', 'n', ',', '小', '女', '子', '不', '才', ',', '未', '得', '公', '子', '青', '睐', ',', ',', ',', '公', '子', '向', '北', '走', ',', '小', '女', '子', '向', '南', '瞧', ',', 'h', 'f', 'k']

s = re.findall("\w",k)
print(s)   # ['s', 'w', 'n', '小', '女', '子', '不', '才', '未', '得', '公', '子', '青', '睐', '8', '8', '8', '6', '6', '6', '公', '子', '向', '北', '走', '小', '女', '子', '向', '南', '瞧', 'h', 'f', 'k']
s = re.findall("\W",k)
print(s)   # [',', ',', ',', ',', ',', ',', ',']

s = re.findall("\s","s swn")
print(s)   # [' ']
s = re.findall("\S","s swn")
print(s)   # ['s', 's', 'w', 'n']

s = re.findall("\w+\s\w+","hfk swn")
print(s)    # ['hfk swn']

s = re.findall("\Aa","a ac")
print(s)  # ['a']

s = re.findall("ac\Z","a ac")
print(s)  # ['ac']
