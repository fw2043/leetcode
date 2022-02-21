"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
nput: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
"""


### Method 1 Intersetction: Using a set to store the visited node, then tranverse each list one by one to find the intersection
# Time Complexity: O(m +n)
# Space Complexity: O( max(n,m))
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headA is not None:
            visited.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in visited:
                return headB
            headB = headB.next

        return None


# Method 2:
# Two pointers to traverse the lists
# If they have same length, then you will meet at the first intersection
# So find the diff and the longer one
# Let the longer one move first diff steps
# Time Complexity: O(m +n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Two pointers to traverse the lists
        # If they have same length, then you will meet at the first intersection
        # Let the longer one move first diff steps
        currA, currB = headA, headB
        # get the lengths for them
        a, b = 0, 0
        while currA:
            a += 1
            currA = currA.next
        while currB:
            b += 1
            currB = currB.next
        # find the long and short lists
        if a > b:
            currLong = headA
            diff = a - b
            currShort = headB
        else:
            currLong = headB
            diff = b - a
            currShort = headA

        while diff > 0:
            currLong = currLong.next
            diff -= 1
        # travese
        while currLong != currShort:
            currLong = currLong.next
            currShort = currShort.next

        return currLong

        return None
