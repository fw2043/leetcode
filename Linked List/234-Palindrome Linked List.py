"""
Given the head of a singly linked list, return true if it is a palindrome.
Input: head = [1,2,2,1]
Output: true
Input: head = [1,2]
Output: false
Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""


# Method 1: Linear using list: space compleity and time complexity: O(N)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next

        l, r = 0, len(arr) - 1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1

        return True


# Method 2: Two pointers:
# Time complexity : O(n), where nn is the number of nodes in the Linked List.
# Space complexity : O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Two pointers
        # head = [1,2,2,1]
        # find the middle: slow
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half: [2,1] ----> [1,2]
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # prev will be the right node:  pev = 1, 1 ---> 2
        # slow is None

        # check if it is    palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
