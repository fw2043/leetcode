"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e.,
only nodes themselves may be changed.)
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save ptrs
            nextpair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nextpair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nextpair

        return dummy.next
