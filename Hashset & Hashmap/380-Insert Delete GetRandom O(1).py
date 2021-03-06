"""
Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present.
Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present.
Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements
(it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
# The idea of GetRandom is to choose a random index and then to retrieve an element with that index.
# Each element must have the same probability of being returned.
# In average O(1) time complexity.

# Approach: Use random.choice(list) method
import random
class RandomizedSet:

    def __init__(self):
        # dict to store value: index
        self.items = {}

    def insert(self, val: int) -> bool:
        if self.items.get(val):
            return False
        self.items[val] = True
        return True

    def remove(self, val: int) -> bool:
        if self.items.get(val):
            self.items.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        # print(self.items)
        return random.choice(list(self.items.keys()))
# Different time complexity using different data structures to implement:
# insert/delete/get item:
# to check if the element exits or not: dict: O(1), array: O(n)
#https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/455253/Python-or-Super-Efficient-or-Detailed-Explanation


# Approach: hashmap and list
# Hashmap/dict
# Time complexity for dict to insert and delete is O(1), but there is no index in dict,we can not get getRandom by index

# Array list has indexes and can do insert and getRandom in O(1), but not for delete
# So to delete value which could be in any position from array list without going through all the list:
# step 1: swap the element to the last one
# step 2: Pop the last element out.

# Hashmap: element -> index pairs
# Array list: all the elements

class RandomizedSet:

    def __init__(self):
        # dict to store value: index
        # Time complexity for dict to insert and delete is O(1), but there is no not for getRandom
        self.dict = {}
        # To store all the items,
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)  # index is the last one == lenght of the current list
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # move the last element to the place idx of the element to delete
        last_element = self.list[-1]
        indx = self.dict[val]
        self.list[indx], self.dict[last_element] = last_element, indx
        # delete the last element: O(1)
        self.list.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        # import random
        return random.choice(self.list)




