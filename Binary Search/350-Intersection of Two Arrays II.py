from typing import List
"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
"""
##########################################################################
# Follow up:
########################################################################


"""
What if the given array is already sorted? How would you optimize your algorithm? --- Binary search
What if nums1's size is small compared to nums2's size? Which algorithm is better? --- call the function itself to search each element  from smaller list
What if elements of nums2 are stored on disk, and the memory is limited 
such that you cannot load all elements into the memory at once?
"""
####################################################################################################
"""
similar to leetcode 349
"""

"""
Method 1: sort the lists and two pointers
Time complexity: O(n + m)
Space complexity: n + m + the length of intersection ===> max: 2(n +m)
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # list can store duplicates, set to store unique value
        result = []
        i = j = 0
        # sort the lists and two pointers
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # list use append, set use add buil-in method
                result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

"""
Method 2: use dictionary to count
time complexity: O(n + m)
Space complexity: choose one O(m) or O(n) <--- So choose the
smaller one if you can
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # list can store deplicates, set only store unique valus
        result = []
        # use dictionary to count
        hashmap = {}
        for num in nums1:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for num in nums2:
            if num in hashmap and hashmap[num] > 0:
                result.append(num)
                hashmap[num] -= 1

        return result
"""
Method 3: Binary Search:
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1.sort()
        result = []
        for index in range(len(nums2)):
            temp = nums2[index]
            start, end = 0, len(nums1) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums1[mid] == temp:
                    result.append(temp)
                    nums1.pop(mid)
                    break
                if nums1[mid] < temp:
                    start = mid - 1
                else:
                    end = mid + 1
        return result

