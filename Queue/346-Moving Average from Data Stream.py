""""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.


Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
"""

# Usually we use queue to stream data, first in first out.
# Queue
# Time complexity: O(n)
# Space complexity: O(n)
class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size

    def next(self, val: int) -> float:

        # add elemenet
        self.q.append(val)
        # check if the len > size, if yes, pop
        if len(self.q) > self.size:
            self.q.popleft()
        total = 0
        for i in range(len(self.q)):
            total += self.q[i]

        return total / len(self.q)
## Can we improve the code above?
## adding count and window_sum into constructor , so we don't have to iterate the list
# Time complexity: O(1)
# Space complexity: O(n)
class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        # keep tracking the total of elements seen so far and keep tracking the sum,
        # so when we run in next() method, we don't need to iterate the queue to get the sum and the length
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1

        # add elemenet
        self.q.append(val)
        # check if the len > size, if yes, pop
        first = 0
        if len(self.q) > self.size:
            first = self.q.popleft()
        self.window_sum = self.window_sum - first + val

        return self.window_sum / min(self.size, self.count)


