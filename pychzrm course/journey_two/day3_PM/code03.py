"""
    基本查找方法
"""

#对有序数列进行二分查找

def search(list_,key):
    low,high = 0,len(list_) -1
    while low <= high:
        mid = (low + high) // 2
        if list_[mid] < key:
            low = mid + 1
        elif list_[mid] > key:
            high = mid -1
        else:
            return mid
l = [1,4,4,5,6,88,99,]
print(search(l,88))