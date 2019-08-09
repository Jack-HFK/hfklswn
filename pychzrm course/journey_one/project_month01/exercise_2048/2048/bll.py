"""
    BLL 业务逻辑层
"""
from model import Location
import random
class GameCoreController:
    """
    游戏核心逻辑处理
    """

    def __init__(self):

        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4
        ]
        #用于储存0和合并的列表
        self.list_merge = []
        # 用于储存空位置的列表
        self.__list_empty_location = []
        #地图是否发生变化
        self.is_change = False
    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, value):
        self.__map = value

    # 1. 定义函数,将列表中0元素移至末尾.

    def zero_to_end(self):
        # 思路:删除0元素,再末尾增加.
        for i in range(len(self.list_merge) - 1, -1, -1):
            if self.list_merge[i] == 0:
                del self.list_merge[i]
                self.list_merge.append(0)
        return self.list_merge

    def merge(self):
        self.zero_to_end()  # [2,0,0,2] -->  [2,2,0,0]
        # 如果相邻且相同相加，删除相邻的，添加一个新的0
        for i in range(len(self.list_merge) - 1):
            if self.list_merge[i] == self.list_merge[i + 1]:
                self.list_merge[i] += self.list_merge[i + 1]
                del self.list_merge[i + 1]
                self.list_merge.append(0)
        self.zero_to_end()

    # def move_left(self, map):
    #     # 思想:将每行(从左向右获取行数据)传递给合并函数
    #     for row in map:
    #         # 传递给merge函数的是二维列表中的元素(一维列表对象地址)
    #         # 函数都是操作对象,所以无需通过返回值拿到操作结果.
    #         self.merge(row)
    # 4.定义函数,向右移动.

    def move_right(self, map):
        # 思想:将每行(从右向左获取行数据)传递给合并函数
        for i in range(len(map)):
            # map[0][::-1] 从右向左获取行数据(新列表)
            list_merge = map[i][::-1]
            self.merge()
            # 将合并后的结果,从右向左获还给二维列表
            map[i][::-1] = self.list_merge

    # 作业1:向上移动(核心思想:从上到下获取列数据,形成一维列表,交给合并方法,最后恢复)
    def move_up(self, map):
        # 00  10  20  30
        # 01  11  21  31
        for c in range(4):
            list_merge = []
            for r in range(4):
                list_merge.append(map[r][c])

            self.merge()

            for r in range(4):
                map[r][c] = list_merge[r]

    # 作业2:向下移动(核心思想:从下到上获取列数据,形成一维列表,交给合并方法,最后恢复)
    def move_down(self, map):
        # 30  20  10  00
        for c in range(4):
            list_merge = []
            for r in range(3, -1, -1):
                list_merge.append(map[r][c])

            self.merge()

            # list_merge(从左到右) 赋值给 二维列表(从下到上)
            for r in range(3, -1, -1):  # 3 2 1 0
                map[r][c] = list_merge[3 - r]

    def __calculate_empty_location(self):
        """
        :return:
        """
        self.__list_empty_location.clear() #clear清空列表
        for r in range(4):
            for c in range(4):
                if self.__map[r][c] == 0:
                    loc = Location(r, c)
                    self.__list_empty_location.append(loc)

    def generate_new_number(self):
        """
        随机生成新数字
        :return:
        """
        # self.__list_empty_location()
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1,10) == 1 else 2
        self.__list_empty_location.remove(loc)