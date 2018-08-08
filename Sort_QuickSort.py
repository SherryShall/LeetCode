# 时间：O(nlogn)
# 空间：O(1)
#coding=utf-8

import sys

sys.setrecursionlimit(1000000)

def quick_sort(array):
    start = 0
    end = len(array) - 1
    act_quick_sort(start, end, array)

def act_quick_sort(start, end, array):
    print(start, end)
    if end - start < 1:
        return
    i = start
    k = end
    for j in range(i, k):
        if array[j] < array[k]:
            array[i], array[j] = array[j], array[i]
            i += 1
    if i == k:
        return
    array[i], array[k] = array[k], array[i]
    # print(start, i)
    # print(i, end)
    act_quick_sort(start, i-1, array)
    act_quick_sort(i+1, end, array)


if __name__ == "__main__":
    # array = [4, 2, 7, 5, 8, 9, 4, 3, 6]
    array = [1, 1, 1, 0, 1, 1, 1]
    quick_sort(array)
    print(array)
