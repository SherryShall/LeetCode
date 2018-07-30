"""
输入：两个整数序列，第一个序列代表栈的压入顺序，判断第二个序列是否为该栈的弹出顺序。
ps：假设所有数字均不相等

例如：[1,2,3,4,5]是某栈的压栈序列,[4,5,3,2,1]是一个弹出序列，但[4,3,5,1,2]不可能是一个弹出序列
"""
#coding=utf-8

def is_pop_order(push_array, pop_array):
    if len(push_array) < len(pop_array):
        return False
    elif len(push_array) == len(pop_array) == 0:
        return True
    i = j = 0
    tmp_stack = [push_array[i]]
    while j < len(pop_array):
        if pop_array[j] != tmp_stack[-1]:
            i += 1
            if i < len(push_array):
                tmp_stack.append(push_array[i])
            else:
                return False
        else:
            tmp_stack.pop()
            j += 1
    return True

if __name__ == "__main__":
    push_array = [1, 2, 3, 4, 5]
    pop_array_1 = [4, 5, 3, 2, 1]
    pop_array_2 = [4, 3, 5, 1, 2]
    # push_array = []
    # pop_array_1 = [1]
    # pop_array_2 = []
    print(is_pop_order(push_array, pop_array_1))
    print(is_pop_order(push_array, pop_array_2))

