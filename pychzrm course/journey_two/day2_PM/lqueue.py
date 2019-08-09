"""
lqueue.py  队列的链式存储
重点代码

思路分析：
1. 基于链表完成存储链式栈
2. 链表的开端作为队头，尾端做为队尾

"""

# 自定义队列异常
class QueueErroy(Exception):
    pass

# 节点类
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 链式队列类
class LQueue:
    def __init__(self):
        #开始头尾指向一个没有实际意义的节点
        self.front = self.rear = Node(None)
    # 初始化空链表
    def is__empty(self):
        return  self.front == self.rear
    # 入队
    def enqueue(self,elem):
        self.rear.next = Node(elem)
        self.rear = self.rear.next
    # 出队，头动
    def dequeue(self):
        if self.front == self.rear:
            raise QueueErroy("Queue is empty")
        self.front = self.front.next
        return self.front.data

if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())
























