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
#### Can you sort the linked list in O(n logn) time: Merge sort and quick sort
# long(n) memory: merge sort
# O(1) memory (i.e. constant space)-------------> Quick sort

##### Merge sort:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sorting with O(nlogn) running time: merge sort and quick sort

        # merge sort  O(nlogn) running time with O(n) momery

        # get the middle:
        # base case:
        if not head or not head.next:
            return head
        # split the list into two halfs:
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        # divide:
        left = self.sortList(left)
        right = self.sortList(right)
        # conquar
        return self.merge(left, right)

    # now we can writeh the functions getMid and merge
    #
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