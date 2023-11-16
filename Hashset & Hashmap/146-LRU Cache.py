"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""
# Approach 1: OrderedDict
# https://docs.python.org/3/library/collections.html#ordereddict-objects
# The OrderedDict was designed to be good at reordering operations
# move_to_end(key, last=True)
# popitem(last=True)

# method 1
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_value = collections.OrderedDict()

    def get(self, key: int) -> int:

        if key in self.key_value:
            # move to the most recent side: right
            self.key_value.move_to_end(key)
            return self.key_value[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists.
        if key in self.key_value:
            # move to the most recent side: right
            self.key_value.move_to_end(key)

        self.key_value[key] = value

        # check capacity
        if len(self.key_value) > self.cap:
            self.key_value.popitem(last=False)
        # print(self.key_value)



# Approach 2:hashmap to store the key,value and double linked list to store least recent used and most recent used?
# hashmap can make get/put with O(1) time complexity
# double linked list can be easy for re-order
"""
key | value
1        2
2        2

However, if the value in the hashmap is to only store value, then when evict happens,  we need to re-order the list, it is hard 
What if:
the value stores a double linked list that it contains the value of the key 
and 
a left point which is to point to the LRU/least recently used key/value
and 
a right point which is to point to the most recently used key/value

key | value
1   |   a node
"""
##### Data strucuture
# a Node include key, value and previous, next node
# a hashmap to map key and a node
# two pointers: left --> LRU, right ---> most recent

# when we put/update or remove a key ---> remove from double linked list, after update the hashmap, then insert into double
# linked list again













