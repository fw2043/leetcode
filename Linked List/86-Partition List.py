"""
Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # listAto store smaller ones, listB to store larger or equal ones
        # Then link A and B together
        # find to identify the new heads and new tails in listA and listB
        # initializetwo dummy nodes as new heads
        # if you write this way: left = right = ListNode(0, None), it means they point to same node
        # but we need them to point to different nodes----> two list
        left, right = ListNode(0, None), ListNode(0, None)
        # initialize new tails
        ltail, rtail = left, right
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        print(left.next)
        print(right.next)

        # update the pointers
        ltail.next = right.next
        rtail.next = None

        return left.next