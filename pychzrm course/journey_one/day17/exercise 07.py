list01 = ["张无忌","赵敏","周芷若"]
list02 = [101,102,103]
for item in zip(list01,list02):
    print(item)
#
def my_zip(list01,list02):
    for key01 in list01:
        for key02 in list02:
            print(key01,key02)

