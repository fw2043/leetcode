"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""
# Clarify
# Hashset: can not contain duplicate values
# how do we handle collisions: rehashing--- chain
# the capacity?
# how many calls would be made to add, remove and contains?
# add: when we add, we need to check capacity
# remove: two situations: the key does not exist or exist, what if the key does not exist? two situations: the key does not exist or exist
# contains: what kind of value we want to return? what if the key does not exist?

"""
first: mod % to determine the index, if there is any collision:
linked list node: same index, val1 -> val2 
index | value
0     | val1 -> val2
1     | 
.     |
.     |
999   |
"""
# Time complexity: O(1)
# Space complexity: O(n)

class ListNode():
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet(object):

    def __init__(self):
        # capacity: this will create indivivual ListNode,
        # if you wirite ListNode(0) * 10 ** 4, it will copy same one value at the same position, it won't create new positions
        self.set = [ListNode(0) for i in range(10 ** 4)]

    def add(self, key):
        # find the index
        index = key % len(self.set)
        # get the head of the linked listnode at index postion
        cur = self.set[index]  # the head
        # find the last node
        while cur.next:
            if cur.next.key == key:  # find a duplicate
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key):
        # find the index
        index = key % len(self.set)
        # get the head of the linked listnode at index postion
        cur = self.set[index]  # the head
        # find the last node
        while cur.next:
            if cur.next.key == key:  # find the key
                cur.next = cur.next.next  # shift to the next position
                return
            cur = cur.next

    def contains(self, key):
        # find the index
        index = key % len(self.set)
        # get the head of the linked listnode at index postion
        cur = self.set[index]  # the head
        # find the last node
        while cur.next:
            if cur.next.key == key:  # find the key
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)





























