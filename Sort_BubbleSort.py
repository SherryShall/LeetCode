# 时间 O(n^2)  最坏O(n^2)  最好O(n)
# 空间 O(1)
# 稳定

def bubble_sort(array):
    def swap(a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

    swap_flag = False
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j+1] < array[j]:
                swap_flag = True
                # print(array[j], array[j+1])
                # array[j+1], array[j] = array[j], array[j+1]
                array[j], array[j+1] = swap(array[j], array[j+1])
                # print(array[j], array[j+1])
        if not swap_flag:
            break
    return array

"""
        冒泡排序改进算法，时间复杂度O(n^2)
        设置flag，当一轮比较中未发生交换动作，则说明后面的元素其实已经有序排列了。
        对于比较规整的元素集合，可提高一定的排序效率。
"""

if __name__ == "__main__":
    print(bubble_sort([3, 6, 1, 2, 8, 4, 9, 9, 10, 8]))
    print(bubble_sort([]))

