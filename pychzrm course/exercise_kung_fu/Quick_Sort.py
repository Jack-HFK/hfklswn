"""#从数列中挑出一个元素,称为 "基准"(pivot),
重新排序数列,所有元素比基准值小的摆放在基准前面,所有元素比基准值大的摆在基准的
后面(相同的数可以到任一边)。在这个分区退出之后,该基准就处于数列的中间位置。这
个称为分区(partition)操作。
递归地(recursive)把小于基准值元素的子数列和大于基准值元素的子数列排序"""


class Quick_Sort:


    # 快速排序 第一个low（基准数）数序列号 high最后一个数序列号
    def quick(self,list,low,high):
        if low < high:
            key = self.sub_sort(list,low,high)
            self.quick(list,low,key-1) # list以基准为分界线的左边部分
            self.quick(list,key+1,high)# list以基准为分界线的右边部分
        return list

    # 完成一轮排序过程
    def sub_sort(self,lists,low,high):
        x = lists[low]  # 基准数
        while low < high:
            while lists[high] >= x and high > low:
                high -= 1
            lists[low] = lists[high]
            # 后面的数
            while lists[low] < x and low < high:
                low += 1
            lists[high] = lists[low]
        lists[low] = x  # 基准书插入
        return low

l = [5,6,8,2,4,]

c = Quick_Sort()
s = c.quick(l,0,len(l)-1)
print(s)
