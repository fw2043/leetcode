# First In First Out
# head and tail
  In which elements are added only from the one side - rear and removed from the other - front
1. initialize a dequeue:

        q = collections.deque() # dequeue class is faster than list or queue for appening and poping elements
2. add: from tail: O(1)

        q.append()
3. delete:

        q.popleft() ---> pop from the head, get the first element from queue: O(1)
        q.pop() ---> pop from the tail, O(1),get the last element from queue: O(1)
4. Implement using queue class:

        from queue import Queue
        # Initializing a queue
        q = Queue(maxsize = 3)
         
        # qsize() give the maxsize
        # of the Queue
        print(q.qsize())
         
        # Adding of element to queue
        q.put('a')
        q.put('b')
        q.put('c')
        # Removing element from queue
        print(q.get())
        print(q.get())
        print(q.get())
        
 5. Message Queue(MQ): producer, consumer, publish and subscribe
 
 6. Other functions/notes:
  
        q = deque()
        cnt = q.count(item) # the count of an item
 7. Could be design questions, like leetcode 1429, 346, 362, 281
 