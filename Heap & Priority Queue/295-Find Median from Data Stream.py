"""
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
"""
# The median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
# SO, if when we add an item, we always keep the list sorted, then if it will be easy to find the median O(n).
# To find the best solution is to how to optimize running time to keep a the list sorted
# Min Heap and Max Heap, add: O(logn), find a mix/max: O(n)
# Small heap(max heap) + large heap(min heap) with around same size
class MedianFinder:

    def __init__(self):
        # two heaps: small heap(max heap), large heap(min heap)
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # O(logN)

        # by default, add the new element to small heap
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small is <= every num in large:
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

            # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.small[0] * -1 + self.large[0]) / 2

