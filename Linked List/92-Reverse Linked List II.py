"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""
"""
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""
"""
Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""
"""
Note: left and right start from 1 not 0
dummy node which is out of this linked list, dummy.next will be one of the list
the edge case could be reverse the fist one:head = [1,2,3,4,5], left = 1, right = 4
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # 1) reach node at position 'left', save leftprev node to reassign
        leftprev, curr = dummy, head
        for i in range(left - 1):
            leftprev, curr = curr, curr.next

        # Now curr = 'left', prev = 'node before left'
        # 2) reverse from left to right
        prev = None  # (initialize prev as Null, so later we can reassign)
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        # update pointers
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next

