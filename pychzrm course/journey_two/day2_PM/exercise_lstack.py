from  lstack import LStack


ls = LStack()

while True:
    exp = input()
    tmp = exp.split(" ")
    for i in tmp:
        if i not in["+","-","p"]:
            ls.push(float(i))
        elif i == "+":
            x = ls.pop()
            y = ls.pop()
            ls.push(y + x)
        elif i == "-":
            x = ls.pop()
            y = ls.pop()
            ls.push(y - x)
        elif i == "p":
            print(ls._top)


