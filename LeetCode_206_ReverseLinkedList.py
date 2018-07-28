"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

#coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代 60ms
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head:
    #         return None
    #     elif not head.next:
    #         return head
    #
    #     preNode = None
    #     actNode = head
    #     nextNode = head.next
    #     while nextNode:
    #         tmpNode = nextNode.next
    #         actNode.next = preNode
    #         preNode = actNode
    #         actNode = nextNode
    #         nextNode = tmpNode
    #     actNode.next = preNode
    #     return actNode

    # 递归？ 56ms
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        elif not head.next:
            return head

        preNode = None
        actNode = head
        nextNode = head.next
        return self.recur(preNode, actNode, nextNode)

    def recur(self, preNode, actNode, nextNode):
        if nextNode:
            tmpNode = nextNode.next
            actNode.next = preNode
            preNode = actNode
            actNode = nextNode
            nextNode = tmpNode
            return self.recur(preNode, actNode, nextNode)
        else:
            actNode.next = preNode
            return actNode

def printLinkList(head):
    while head:
        print('%f\n' % head.val)
        head = head.next

if __name__ == "__main__":
    solution = Solution()
    # head = None

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    new_head = solution.reverseList(head)

    printLinkList(new_head)
