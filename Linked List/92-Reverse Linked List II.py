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

# Note: left and right start from 1 not 0
# the edge case could be reverse the fist one:head = [1,2,3,4,5], left = 1, right = 4
# 1) reach node at position 'left', save leftprev node to reassign
# 2) reverse from left to right
# 3) connect the prevleft and the reversed part
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = prevleft = ListNode(0, head)
        curr = head
        # head = [1,2,3,4,5], left = 2, right = 4
        # find the curr = left(2), and prevleft = previous node of left(1)
        for i in range(left - 1):
            curr = curr.next
            prevleft = prevleft.next
        # reverse this part:
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # connect the prevleft and the reserved part:
        # node(2) point to node(5)
        prevleft.next.next = curr
        # node(1) point to node(4)
        prevleft.next = prev

        return dummy.next


