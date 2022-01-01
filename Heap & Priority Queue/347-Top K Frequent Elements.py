"""
Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
# Heap:
# Time complexity: O(Nlogk)
# Space complexity:O(N+k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # O(1) time
        if k == len(nums):
            return nums
        # heap
        # input:  nums = [1,1,1,2,2,3], k = 2
        # O(N) time
        count = Counter(nums)
        # count = {1: 3, 2: 2, 3:1}
        # buit-in function
        return heapq.nlargest(k, count.keys(), key=count.get)




# Bucket sort:
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort: count each item occurs
        # the worst case, every nums only appears once, so the length of bucket(count[i]) == length of the nums
        # for example: [1,2,3,4,5,6,7,8,....100]
        # a dict to count each item occurs
        count = {}
        #
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # count = {1:3, 2:2, 3: 1}
        for n, c in count.items():
            freq[c].append(n)
        # freq =[[3],[2], [1]]
        res = []
        for i in range(len(freq) - 1, 0, -1):  # reversere from last to first
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

