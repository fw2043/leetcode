"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
"""
# Clarify:
"""
how many calls ---> capacity
data type of key: integer ---> mapping key % 1000 ---> index
collisions: 1000 and 11000 ----> open addressing or chaining ----> chaining is easier to implement
for example:
100 1
1100 2
index | value
100      1 -> 2
"""


class ListNode():
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hashing(self, key):
        return key % len(self.map)

    def put(self, key, value):
        cur = self.map[self.hashing(key)]
        # two stituations: new key or the key exist, only need to update the value
        while cur.next:  # cur will point to the last node after the loop so that we can put the new node next to it
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key):
        cur = self.map[self.hashing(key)]
        # two stituations: new key or the key exist, only need to update the value
        while cur:  # cur will point to null when reaching out to the loop end
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        cur = self.map[self.hashing(key)]
        # two stituations: new key or the key exist, only need to update the value
        while cur.next and cur.next != key:  # cur will stop right before the node we want to delete
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)












