#### Top: 
Stack is LIFO (last in - first out) data structure, 
in which elements are **added and removed from the same end**, called top (a pointer keep changing while pushing items)

In python, you can just use list
        
        add: push()--->O(1)
        delete: pop() --->O(1)
        Retrieves the top without removing: peek()
#### Since a stack will remove elements in the reverse order that it inserted them in
stack.push(1)
stack.push(2)
stack.push(3): [1,2,3]
stack.pop()  --> 3
stack.pop()  --> 2
stack.pop() ---> 1






#### Approach:
1) Stack and hashmap
2) Stack and a current point: 1472 Design Browser History
3) Two stacks: 155 min stack, 1472 Design Browser History
4) Stack with list of list: [['a', 1], ['c', 2], ['d', 3]], like 1209

