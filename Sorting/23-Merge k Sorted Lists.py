"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
# Confirm that the output is linked-list
# Approach 1: Brute Force:
# Time complexity: O(NlogN)
# Space complexity: O(N).

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case:
        if len(lists) < 1:
            return

        self.nodes = []
        # Initilazie dummy nodes to get the head and trverse the nodes:
        head = point = ListNode(0, None)

        # put the elements into a list
        for l in lists:
            # print(l.val)
            while l:
                self.nodes.append(l.val)
                # print(l.val)
                l = l.next
        # sort the list:
        self.nodes = sorted(self.nodes)

        # convert the sorted list to linked-list:
        for x in self.nodes:
            point.next = ListNode(x)
            point = point.next

        return head.next

# Approach 2:
# how to merge two sorted linked list: leetcode 21
# now 2 becomes k, but we can use the similar solution:
# divide and conquer:
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case:
        if not lists or len(lists) < 1:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None  # out of bound
                mergedLists.append(self.merge2lists(l1, l2))
                # print(i, mergedLists)
            # update the lists to interation
            lists = mergedLists

        return lists[0]

    def merge2lists(self, l1, l2):
        dummy = tail = ListNode(0, None)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
# Time complexity : O(Nlogk)


