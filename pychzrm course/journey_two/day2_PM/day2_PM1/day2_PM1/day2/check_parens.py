from day2.sstack import SStack

text = "Open source software is made better when users (can easily) contribute code and [documentation] to fix bugs and add {fea(tures).} Python {strongly} encoura[ges community] (in{vo}lv[em]ent) in improving the software. Learn more about how to make Python better for everyone."

parens = "{}[]()"  #　需要验证的字符
left_parens = "{[("
#　验证配对是否正确
opposite = {'}':'{',']':'[',')':'('}

st = SStack() #　初始化一个栈

# 负责提供遍历到的括号
def parent(text):
  """
  遍历字符串,提供括号字符和其位置
  """
  #　ｉ记录索引位置
  i,text_len = 0,len(text)
  while True:
    # 循环遍历字符串
    # 到结尾结束，遇到括号提供给ｖｅｒ
    while i < text_len and text[i] not in parens:
      i += 1

    if i >= text_len:
      return
    else:
      yield  text[i],i
      i += 1


#　字符是否匹配的验证工作
def ver():
  for pr, i in parent(text):
    if pr in left_parens:
      st.push((pr,i))  #　左括号入栈
    elif st.is_empty() or st.pop()[0] != opposite[pr]:
      print("Unmatching is found at %d for %s"%(i,pr))
      break
  #　ｆｏｒ循环正常结束
  else:
    if st.is_empty():
      print("All parentheses are matched")
    else:
      #　剩下左括号了
      p = st.pop()
      print("Unmatching is found at %d for %s" % (p[1], p[0]))

# 主程序只负责做括号的验证
ver()









