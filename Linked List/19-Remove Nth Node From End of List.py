"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
"""
# Get the length(go through the list)
# identify the previous node
# previous.next = previous.next.next

# Can we optimize the slution above using one pass: Yes, find the left and right node of the deleted node
# let left = dummy, right=head, then let right move n steps, then move right and left until right is null
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = prev = ListNode(0, head)
        curr = head
        while curr:
            size += 1
            curr = curr.next
        # find the previous
        step = size - n
        while step > 0:
            prev = prev.next
            step -= 1
        prev.next = prev.next.next

        return dummy.next


# Two pointer( left and right to point to the left and right nodes of the delete one):

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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