# First In First Out
# head and tail
  In which elements are added only from the one side - rear and removed from the other - front
1. initialize a queue:
    q = deque()
2. add: from tail: O(1)
    q.append()
3. delete: from head: O(n)
    q.popleft() ---> pop from the head
    1.pop() ---> pop from the tail
4. update: