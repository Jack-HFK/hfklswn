"""
bitree.py 二叉树的实现

思路分析：　
1. 使用链式存储
　　节点类设计上有两个属性变量引用左孩子和右孩子
2. 操作类完成二叉树的遍历
"""


# 二叉树节点
class TreeNode:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

# 　二叉树操作
class Bitree:
  def __init__(self, root=None):
    self.root = root  # 获取树根

  #　先序遍历
  def preOrder(self,node):
    if node is None:
      return
    print(node.data,end=' ')
    self.preOrder(node.left)
    self.preOrder(node.right)

  # 　中序遍历
  def inOrder(self, node):
    if node is None:
      return
    self.inOrder(node.left)
    print(node.data, end=' ')
    self.inOrder(node.right)


if __name__ == "__main__":
  # 　后序遍历　ＢＦＧＤＩＨＥＣＡ
  # 构建树 (笔记中)
  b = TreeNode('B')
  f = TreeNode('F')
  g = TreeNode('G')
  d = TreeNode('D', f, g)
  i = TreeNode('I')
  h = TreeNode('H')
  e = TreeNode('E', i, h)
  c = TreeNode('C', d, e)
  a = TreeNode('A', b, c)  # 树根

  # 　初始化树对象，得到树根
  bt = Bitree(a)
  #　先序
  bt.preOrder(bt.root)
  print()
  # 　中序
  bt.inOrder(bt.root)
  print()
