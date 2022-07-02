# A priority queue is an abstract data type, while a Heap is a data structure. 
# Therefore, a Heap is not a Priority Queue, but a way to implement a Priority Queue.
# Definition of Heap
According to Wikipedia, a Heap is a special type of binary tree. A heap is a binary tree that meets the following criteria:

Is a complete binary tree;

The value of each node must be no greater than (or no less than) the value of its child nodes.
A Heap has the following properties:

1. Insertion of an element into the Heap has a time complexity of O(logN);

2. Deletion of an element from the Heap has a time complexity of O(logN);

3. The maximum/minimum value in the Heap can be obtained with O(1) time complexity.

# Python buit-in module
1. headq: min-heap, start from index = 0

2. method:

    convert a list to a heap: 
    heapq.heapify()
    
    list = [5, 7, 9, 1, 3]
    
    heapq.heapify(list)

 add an element and maintain the heap: heapq.heappush()

    heapq.heappush(list, 4)
    
  pop the smallest element:
  
    heapq.heappop(list)
    
  Nth largest/smallest element in the list:
  
    heapq.nlargest(3, list1)
    heapq.nsmallest(3, list2)
   
 # Appication:
 1. Heap Sort:
 
    Time complexity: O(NlogN)

    Space complexity: O(N)
 
 2. The Top-K problem
 3. The k-th element
 4. Most frequent problem: Counter() & maxHeap, like 767 and 347
 