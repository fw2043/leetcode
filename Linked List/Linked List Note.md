# Singly Linked List
## 1. Head to represent the whole list
## 2. Traverse: O(N)
If we want to get the ith element, we have to traverse from the head node one by one. It takes us O(N) time on average to visit an element by index, where N is the length of the linked list.
## 3. Add a node: **O(1)**
To add a node(curr) to the prev node:

curr.next = prev.next; 

prev.next = curr

## 4. Add a node at the beginning: **O(1)**
curr.next = head

head = curr

## 5. Delete a (curr) node: **O(N)**: leetcode 237
To delete the current node, we have to find the previous node of the current node: travese from the head:

## 6. Delete the first node:
head = head.next

## 7. Reverse linked list:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
## 8. Cycle linked list: leetcode 141 and 142
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

## 9. Why do we usually need a dummy node?
To deal with lots of edge case, for example insert a node before the head?
How to set dummy node: dummy = ListNode(0, head)

## 10. Relink 3 node in the linked list:
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







**Note**

**when cur = head**
1. while cur: ----> at the end of the loop, cur will point to null
2. while cur.next: -----> at the end of the loop, cur will point to the last node
3. while cur.next and cur.next != key: # cur will stop right before the node we want to delete








