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

