"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e.,
only nodes themselves may be changed.)
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""
# dummy node to return the head
# two pointers for swapping (firstNode and secondNode) and use head to go through each pair
# first=head= 1, second = head.next = 2, then head=firs=3, second=4



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head and head.next:
            # node to be swapped
            firstNode = head
            secondNode = head.next

            # swap the node:
            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            # update head node:
            prev = firstNode
            head = prev.next
        return dummy.next

