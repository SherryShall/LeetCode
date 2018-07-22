# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = self.hasCycle(head)
        if fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
        return fast

    def hasCycle(self, head):
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return fast
        except:
            return None

if __name__ == "__main__":
    solution = Solution()
    solution.detectCycle(head=None)