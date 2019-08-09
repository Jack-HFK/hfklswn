"""
latack.py   栈的链式存储
重点代码
思路分析：
1 基本的实现模型源于 链表
2 栈顶位置

"""


#  自定义异常类
class StackError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 栈操作类
class LStack:
    def __init__(self):
        # 定义栈顶位置属性
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        self._top = Node(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackError("_top is None")
        vasul = self._top
        self._top = self._top.next
        return vasul

    def top(self):  # 查看栈顶值
        if self._top is None:
            raise StackError("_top is None")
        return self._top.data


if __name__ == "__main__":
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    print(ls.top())
    ls.pop()
    print(ls.top())








