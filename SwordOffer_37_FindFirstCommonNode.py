# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        tmpNode1 = pHead1
        tmpNode2 = pHead2
        count1 = count2 = 0
        while tmpNode1:
            count1 += 1
            tmpNode1 = tmpNode1.next
        while tmpNode2:
            count2 += 1
            tmpNode2 = tmpNode2.next
        long_step = count1 - count2
        if long_step > 0:
            for i in range(long_step):
                pHead1 = pHead1.next
        else:
            for i in range(-long_step):
                pHead2 = pHead2.next
        while pHead1 and pHead2:
            if pHead1 == pHead2:
                break
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return pHead1
