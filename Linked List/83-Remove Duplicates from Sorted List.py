"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Input: head = [1,1,2]
Output: [1,2]
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
#### sorted in ascending order
### ending condition: currnode is not None and currnode.next is not None (if any of them is none, then they are not deplicate)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currnode = head
        while currnode is not None and currnode.next is not None:
            if currnode.val == currnode.next.val:
                currnode.next = currnode.next.next
            else:
                currnode = currnode.next

        return head

