"""
练习，一段文字，在文字中可能存在配对错误的情况
    要求写一段代码检测这段文字中有没有括号书写错误，括号包括{}【】（）
"""
from code01 import SStack

parens = "{} [] ()"
left_parens = "{[("
right_parens = "]})"
# 判断配对是否成功
opposite = {"}": "{", "]": "[", ")": "(", }
st = SStack()  # 初始化


# 负责提供遍历到的括号
def parent(text):
    """
    遍历字符串，提供括号字符和其其位置
    :return:
    """
    i, text_len = 0, len(text)
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        if i > text_len:
            return
        else:
            yield text[i], i
            i += 1


# 字符是否匹配的验证工作
def ver():
    for pr, i in parens:
        if pr in left_parens:
            st.push(pr,i)
        elif st.is_empty() or st.pop()[0] != opposite[pr]:
            print("不匹配出错位置是%d" % i)
            break
    else:
        if st.is_empty():
            print("全部匹配")
        else:
            p = st.top()
            print(p[0],p[1])






        # 主程序只负责括号的验证


ver()
