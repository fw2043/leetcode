"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.


Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
"""

####The key is to set Time complexity for showFirstUnique() to be constant?
#Approach 1: Queue and HashMap of Unique-Status
"""
The goal is to find a fast way o retrieve the first unique integer in the queue, not to add them to the queue!!
1. This particular number has never been seen before now. 
Add it to isUnique with a value of true. Also, add it to the queue.

2. This particular number has already been seen by isUnique, with a value of true. 
This means that the number was previously unique (and is currently in the queue), 
but with this new addition, it no longer is. Update its value to false. Do not add it to the queue.

3. This particular number has already been seen by isUnique, 
with a value of false. 
This means that it has already been seen twice before. 
We don't need to do anything, and shouldn't add it to the queue.-----> the goal is not about adding element
"""
# Constructor: O(K)O(K).
# Add(): Time complexity: O(1)
# showFirstUnique(): O(1)
# Space complexity: O(n)
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.is_unique = {}
        # adding the nums into queue
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # remove all the nums which are not unique from left of queue until we meet the first unique value:
        while self.q and not self.is_unique[self.q[0]]:
            self.q.popleft()

        if self.q:
            return self.q[0]
        return -1

    def add(self, value: int) -> None:
        # case 1: new value, have not seen before:
        if value not in self.is_unique:
            self.q.append(value)
            self.is_unique[value] = True
        # case 2: it has been seen before but it is unique(True), change to false, but not need to add to queue
        elif self.is_unique[value] == True:
            self.is_unique[value] = False
        # case 3: if it has been seen two times before(unique = false), do nothing


# Appraoch 3: Brute Forece---> bad idea
# Time complexity for showFirstUnique is O(n^2)
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)

    def showFirstUnique(self) -> int:
        for item in self.q:
            # use queue.count(item) method
            if self.q.count(item) == 1:
                return item
        return -1

    def add(self, value: int) -> None:
        self.q.append(value)

