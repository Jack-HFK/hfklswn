"""
二叉树实现
思路分析
    1.使用链式存储
        节点类设计上有两个属性变量引用左子树和右子树
    2.操作类完成二叉树的遍历
"""


from day2_PM1.squeue import SQueue
# 二叉树节点
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 二叉树操作类
class Bitree:
    def __init__(self, root=None):
        self.root = root
        self.list01 = []
    # 先序遍历
    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    # 中序遍历
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    # 后序遍历
    def laterorder(self, node):
        if node is None:
            return
        self.laterorder(node.left)
        self.laterorder(node.right)
        print(node.data, end=" ")

    # 层次遍历
    def levelorder(self, node):
        sq = SQueue()
        sq.enqueue(node) #从node遍历
        while not sq.is_empty():
            node = sq.dequeue() # 出队一个
            print(node.data,end=" ") #遍历数据
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)
if __name__ == "__main__":
    # 后序方式遍历 BFGDIHECA
    b = TreeNode("B")
    f = TreeNode("F")
    g = TreeNode("G")
    d = TreeNode("D", f, g)
    i = TreeNode("I")
    h = TreeNode("H")
    e = TreeNode("E", i, h)
    c = TreeNode("C", d, e)
    a = TreeNode("A", b, c)
    # 初始化树对象，得到树根
    bt = Bitree(a)
    # 先序调用
    bt.preorder(bt.root)
    print()
    # 中序调用
    bt.inorder(bt.root)
    print()
    bt.laterorder(bt.root)
    print()
