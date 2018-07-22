class Solution(object):
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if not head or not head.next or not head.next.next:
    #         return False
    #     singleP = head.next
    #     doubleP = head.next.next
    #     while singleP and doubleP:
    #         if singleP == doubleP:
    #             return True
    #         else:
    #             if singleP.next and doubleP.next and doubleP.next.next:
    #                 singleP = singleP.next
    #                 doubleP = doubleP.next.next
    #             else:
    #                 return False
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

if __name__ == "__main__":
    slution = Solution()