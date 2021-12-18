"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
"""
### One Pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = curr = ListNode(0, head)
        while curr:
            size += 1
            curr = curr.next

        step = size - n
        prev = dummy
        # get the previous node: 3
        while step > 1:
            step -= 1
            prev = prev.next

        # remove node 4:
        # print(prev)
        prev.next = prev.next.next
        # print(prev)

        return dummy.next


# Two pointer( left and right to point to the left and right nodes of the delete one:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = left = ListNode(0, head)
        right = head
        # let right pointer to move n step
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next

        return dummy.next