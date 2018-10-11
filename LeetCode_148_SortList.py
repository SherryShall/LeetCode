"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.merge(l1, l2)

    def merge(self, node1, node2):
        if node1 is None:
            return node2
        elif node2 is None:
            return node1
        else:
            if node1.val < node2.val:
                node1.next = self.merge(node1.next, node2)
                return node1
            else:
                node2.next = self.merge(node2.next, node1)
                return node2
