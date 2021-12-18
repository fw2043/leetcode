"""
Given the head of a linked list, rotate the list to the right by k places.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

"""
## edge case: empty list
## edge case: what if K is larger than the size

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # empty case
        if not head:
            return head
        # what if K is larger than the size----> have to get the length,  then k = k % length
        length, tail = 1, head
        # why tail.next, not tail,
        # because by the end of this loop, we want the tail point to the last node not null
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        # if k % length ==0, then the rotation does not change the list
        if k == 0:
            return head

        # move to the pivot
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        # rotate
        newhead = curr.next
        curr.next = None
        tail.next = head

        return newhead