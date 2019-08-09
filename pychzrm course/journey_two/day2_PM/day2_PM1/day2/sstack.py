"""
sstack.py 栈模型顺序存储
重点代码

思路分析：
1. 列表即顺序存储，但是功能太多，不符合栈模型
2. 利用列表，封装类，提供栈的接口方法
"""

#　自定义异常类
class StackError(Exception):
  pass

# 顺序栈类封装
class SStack:
  def __init__(self):
    #　属性为空列表，这个列表就是栈的存储空间
    # 列表最后一个元素为栈顶元素
    self._elems = []

  # 判断栈是否为空
  def is_empty(self):
    return self._elems == []

  #　入栈 elem
  def push(self,elem):
    self._elems.append(elem)

  #　出栈
  def pop(self):
    # self._elems为空则ｉｆ语句为真
    if not self._elems:
      raise StackError("stack is empty")
    return self._elems.pop() #　弹出列表最后一个

  #　查看栈顶元素
  def top(self):
    if not self._elems:
      raise StackError("stack is empty")
    return self._elems[-1]

if __name__ == "__main__":
  st = SStack()  #　初始化栈
  st.push(10)
  st.push(20)
  st.push(30)
  while not st.is_empty():
    print(st.pop())









