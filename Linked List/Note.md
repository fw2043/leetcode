# singly linked list
## 1. head to represent the whole list
## 2. traverse: O(N)
If we want to get the ith element, we have to traverse from the head node one by one. It takes us O(N) time on average to visit an element by index, where N is the length of the linked list.
## 3. add a node: **O(1)**
To add a node(curr) to the prev node:

curr.next = prev.next; 

prev.next = curr

## 4. add a node at the beginning: **O(1)**
curr.next = head

head = curr

## 5. delete a (curr) node: **O(N)**
To delete the current node, we have to find the previous node of the current node: travese from the head:

## 6. delete the first node:
head = head.next

## 7. cycle linked list: 
Method 1: two-pointer in linked list:
If there is no cycle, the fast pointer will stop at the end of the linked list. 
If there is a cycle, the fast pointer will eventually meet with the slow pointer.

**Attention: the ending condition**

Method 2: hash table:
using a hash table to store node, not node.val, what if they have some values

        nodes_seen = set()
        
        while head is not None:
        
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next    
        return False

## https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1216/

## 8. Why do we usually need a dummy node?
To deal with lots of edge case, for example insert a node before the head?
How to set dummy node: dummy = ListNode(0, head)

## 9. relink 3 node in the linked list:
    prev.next = curr.next
    curr.next = temp.next
    temp.next = curr
    # advance curr node
    curr = prev.next



**Linked List is all about the link, how to link them, like leetcode92**
**most time you need to change the links(next), but sometimes you might just need to swap/change values**

**Either hashtable or two pointers**


**The difference between left = right = ListNode(0, None) AND left, right = ListNode(0, None), ListNode(0, None):**

    One list with two pointers or Two separated lists 
















