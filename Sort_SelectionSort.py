'''
简单选择排序（simple selection sort）:
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：不稳定

对尚未完成排序的所有元素，从头到尾比一遍，
记录下最小的那个元素的下标，也就是该元素的位置,再把该元素交换到当前遍历的最前面。
其效率之处在于，每一轮中比较了很多次，但只交换一次。因此虽然它的时间复杂度也是O(n^2)，但比冒泡算法还是要好一点。
'''

def selection_sort(array):
    for i in range(len(array)):
        min_num_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_num_index]:
                min_num_index = j
        if min_num_index != i:
            array[i], array[min_num_index] = array[min_num_index], array[i]
    return array

if __name__ == "__main__":
    print(selection_sort([3, 6, 1, 2, 8, 4, 9, 9, 10, 8]))
    print(selection_sort([]))