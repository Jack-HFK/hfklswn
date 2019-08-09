"""
lqueue.py 链式队列
重点代码

思路分析：
1. 基于链表模型完成链式栈
2. 链表开端作为队头，尾端作为队尾
"""

# 　自定义队列异常
class QueueError(Exception):
  pass

#节点类
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# 链式队列类
class LQueue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self,elem):
    node = Node(elem)
    self.front = self.rear = node


