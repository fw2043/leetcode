"""
Given the head of a linked list, return the list after sorting it in ascending order.
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""
# The result is still a linked list!

# Merge sort:
# how to get middle for a linked list:
# how to separate a linked list into 2:
# how to merge two linked list:
# to store a new linked list: dummy = tail = ListNode(), return dummy.next, use tail to traverse


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base case:
        if not head or not head.next:
            return head
        # split the list into two halfs:
        left = head
        # iniliaze right to middle node
        right = self.getMid(head)
        # get mid: if the list is: 4 --> 2 --> 1 ---> 3, the mid == 2, but we want the right == 3!
        # also we want separate them to two lists: 4 ---> 2(right) and 1 ---> 3
        tmp = right.next
        right.next = None # to separate into two node
        right = tmp

        # divide:
        left = self.sortList(left)
        right = self.sortList(right)

        # conquar
        return self.merge(left, right)

    # now we can write the functions getMid and merge:
    # get mid: if the length of list is even, the mid will be the first one, but we want the second one
    # like: 4 --> 2 --> 1 ---> 3, the mid == 2, but we want the right == 3!
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # merge
    def merge(self, left, right):
        dummy = tail = ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next