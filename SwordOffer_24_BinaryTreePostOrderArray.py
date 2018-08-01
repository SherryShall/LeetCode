"""
给定一个整数数组，判断是不是某二叉搜索树的后序遍历的结果。
return True or False
"""

array = [5, 7, 6, 9, 11, 10, 8]

def is_post_order(array):
    if not array:
        return True

    def judge(start, end, array):
        if end - start < 1:
            return True
        root = array[end]
        left_flag = True
        right_flag = True
        right_st = start
        for i in range(end):
            if array[i] > root:
                for j in range(i, end):
                    if array[j] < root:
                        right_flag = False
                        break
                if right_flag:
                    right_st = i
                break
        if left_flag and right_flag:
            return judge(start, right_st-1, array) and judge(right_st, end-1, array)
        else:
            return False

    return judge(0, len(array)-1, array)

if __name__ == "__main__":
    array = [5, 7, 6, 9, 11, 10, 8]
    array = [7, 4, 6, 5]
    array = [0]
    print(is_post_order(array))