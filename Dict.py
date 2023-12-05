# Create a dict:
dict = {}
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using key
print(Dict['name'])
print(Dict[1])

# Get vaule
print(Dict.get(3))

# .keys(): Returns list of dictionary dict’s keys
# output: [1, 'name', 3]
# .items(): return the list with all dictionary keys with values.
# Dictionary with three items
Dictionary1 = {'A': 'Geeks', 'B': 4, 'C': 'Geeks'}
print(Dictionary1.items())
# output: dict_items([('A', 'Geeks'), ('B', 4), ('C', 'Geeks')])
# to iterate it:
for i, n in dict.items():
    freq[c].append(n)


# Counter:
# for a list
list1 = [1,9,9,5,0,8,0,9]
print(Counter(list1))
# output: {9:3, 0:2, 1:1, 5:1, 8:1}

# for a string
temp = Counter('aabbc')
print(temp)
#output: {'a': 2, 'b': 2, 'c': 1}


count = Counter(s)  # hashmap: {'a': 3, 'b': 1}
# maxHeap: {[-3,'a'], [-1, 'b']}, put [-3,'a'], instead of ['a', 3] for sorting purpose and also max: * -1
maxHeap = [[-cnt, char] for char, cnt in count.items()]
heapq.heapify(maxHeap)

count = Counter(words)
count = sorted(count, key=lambda x:count[x], reverse=True)

# defaultdict
from collections import defaultdict
nei = collections.defaultdict(list)
# add beginWord to the wordlist:
wordList.append(beginWord)
# fill the dictionary
for word in wordList:
    for j in range(len(word)):
        pattern = word[:j] + "*" + word[j + 1:]
        # print(pattern)
        nei[pattern].append(word)
        # print(nei)
# Lambda
manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
n, c = len(points), collections.defaultdict(list)
for i in range(n):
    for j in range(i+1, n):
        d = manhattan(points[i], points[j])
        c[i].append((d, j))
        c[j].append((d, i))
# dict:
dict.items() # [(key, value), (...)]
dict.keys() # [key...]
dict.values() # [value...]


# Sort a dict by key
key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
# the return value for sorted(key_value) is the list of the keys: [1, 2, 3, 4, 5, 6]
for i in sorted(key_value):
    print(i, key_value[i])
sorted(key_value, reverse = True) # [6, 5, 4, 3, 2, 1]

# sort by value: [(1, 2), (5, 12), (6, 18), (4, 24), (2, 56), (3, 323)]
list = sorted(key_value.items(), key=lambda item: item[1])
# items will be a list: [(2, 56), (1, 2), (5, 12), (4, 24), (6, 18), (3, 323)]
# item[1] means value, item[0] means key
for key, value in sorted(key_value, key=lambda item: item[1]):
    print((key, value))

# Combine the values of two dictionaries having same key
from collections import Counter
ini_dictionary1 = Counter({'nikhil': 1, 'akash' : 5,'manjeet' : 10, 'akshat' : 15})
ini_dictionary2 = Counter({'akash' : 7, 'akshat' : 5,'m' : 15})

 #combining dictionaries
# using Counter
final_dictionary = ini_dictionary1 + ini_dictionary2