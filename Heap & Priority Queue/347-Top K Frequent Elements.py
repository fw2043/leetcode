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
# Clarify:
# what is we have multiple answers?
# what is k >= len(nums)

# ege case: k = len(nums)


# Approach 1: Heap:
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



# Approach 2: Brute Force:
# bucket sort: count each item occurs
# the worst case, every nums only appears once, so the length of bucket(count[i]) == length of the nums
# for example: [1,2,3,4,5,6,7,8,....100]
# a dict to count each item occurs
# Time complexity: O(n * K) ====> worst case: O(n^2)
# Space complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {n: freq}
        cnt = {}
        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)

        # sort the cnt by freq
        freq = sorted(cnt.values(), reverse=True)
        res = []
        for i in range(k):
            for n in cnt:
                if cnt[n] == freq[i] and n not in res:
                    res.append(n)
        return res




