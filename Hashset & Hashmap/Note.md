# Data strcutures in collections:
https://docs.python.org/3/library/collections.html#
1. Counter:

        counts = collection.Counter(nums1)
       # same to dict:
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
2. deque:
3. OrderedDict: was designed to be good at reordering operations, easy to move/pop the item from the most left/right
 
        dict = collections.OrderedDict() # initialize
        dict.popitem(last=False) # remove the leftmost
        dict.popitem(last=True) # remove the rightmost
        dict.move_to_end(key, last=True) # move the key/value to the mostright
        dict.move_to_end(key, last=False) # move the key/value to the leftmost
        dict.values() # get the list of values
        dict.keys() # get the list of keys

# Hashmap: 
**Time complexity for insert and delete is: O(1)**
 

 # Hash set:
 Initialize: hashset = set()
 
 Add: hashset.add(value)
 


# note: 

s = 'eat'

sorted(s) ====> ['a', 'e', 't']

sorted_string = ''.join(sorted(s))  ===> 'aet'
