import csv


# writerow写入一行
with open("test.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["步惊云","30"])
    writer.writerow(["聂风","28"])

# writerows([(),(),()]) 参数为列表：每个()表示一行 newline="":新的一行
with open("test.csv","a+",newline="") as f :
    writer = csv.writer(f)
    writer.writerows([("聂风","30",5),("第二梦","25","30")])
