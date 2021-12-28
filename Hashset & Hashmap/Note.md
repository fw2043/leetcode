# Hashmap:
# TIme complexity for inset and delete is: O(1)
 Initialize: prevMap = {}
 
 Add:  prevMap[value] = index
 
 
 
 
 # Hash set:
 Initialize: hashset = set()
 
 Add: hashset.add(value)
 
 # OrderedDict
 https://docs.python.org/3/library/collections.html#ordereddict-objects

The OrderedDict was designed to be good at reordering operations
To initialize:

    collections.OrderedDict()
To move any item to end: 
    
    move_to_end(key, last=True)
To pop any item:

    pop(key)  
To pop right or left item:
    
    popitem(last=True)
    
# note: 

s = 'eat'

sorted(s) ====> ['a', 'e', 't']

sorted_string = ''.join(sorted(s))  ===> 'aet'
