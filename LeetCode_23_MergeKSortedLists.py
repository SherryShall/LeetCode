"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		self.checkListNode(lists)
		# N个结点分K个链表
		# 归并 O(NK) %7.46
		# return self.mergeSortMethod(lists)

		# 最小优先队列 O((N+K)lgK  一次建堆 KlgK + N次维护 N*lgK   N>=K  时间复杂度≈O(NlogK)
		# 12.25%
		return self.minHeapMethod(lists)

	def checkListNode(self, lists):
		i = 0
		while i < len(lists):
			if not lists[i]:
				del lists[i]
			else:
				i += 1

#------------------------------------------------------------------
	def mergeSortMethod(self, lists):

		def getMinNodeIndex(lists):
			min_val = lists[0].val
			index = 0
			for i in range(1, len(lists)):
				if lists[i].val < min_val:
					min_val = lists[i].val
					index = i
			return index

		head = ListNode(0)
		tmp = head
		while lists:
			min_index = getMinNodeIndex(lists)
			tmp.next = lists[min_index]
			tmp = tmp.next
			lists[min_index] = lists[min_index].next
			if not lists[min_index]:
				del lists[min_index]
		return head.next

# ------------------------------------------------------------------
	def minHeapMethod(self, lists):
		def minHeapify(lists, pos): #pos range from [1, len(lists)]
			left_pos = pos * 2
			right_pos = pos * 2 + 1
			if left_pos > len(lists):
				return

			if lists[pos-1].val > lists[left_pos-1].val:
				minist = left_pos
			else:
				minist = pos
			if right_pos <= len(lists) and lists[minist-1].val > lists[right_pos-1].val:
				minist = right_pos

			if minist != pos:
				lists[minist-1], lists[pos-1] = lists[pos-1], lists[minist-1]
				# print(minist)
				# print([node.val for node in lists])
				minHeapify(lists, minist)

		def buildMinHeap(lists):
			L = len(lists)
			for pos in range(L//2, 0, -1):
				minHeapify(lists, pos)

		head = ListNode(0)
		tmp = head
		# print([node.val for node in lists])
		buildMinHeap(lists)
		# print([node.val for node in lists])
		while lists:
			minHeapify(lists, 1)
			tmp.next = lists[0]
			tmp = tmp.next
			if lists[0].next:
				lists[0] = lists[0].next
			else:
				lists[0] = lists[-1]
				del lists[-1]
		return head.next