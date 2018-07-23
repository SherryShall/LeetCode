'''
直接插入排序
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定

基本操作是将后面一个记录插入到前面已经排好序的有序表中
'''

def insert_sort(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            j = i-1
            tmp = array[i]
            while j >= 0 and tmp < array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = tmp
    return array

if __name__ == "__main__":
    print(insert_sort([3, 6, 1, 2, 8, 4, 9, 9, 10, 8]))
    print(insert_sort([]))
