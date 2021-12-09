"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Constraints:

1 <= arr.length <= 1000 (not too long)
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""
##################################################################################
##############################################
## Solution
"""
Brute Force
O(N) -------> checking each postive interger to compare with each item in the array
"""
# iInput: arr = [2,3,4,7,11], k = 5
"""
step1: num = 1:
        compare arr[0] ?= num     2 ?= 1  
        k -= 1 = 4    ------> found one missing value
        result = num = 1 ------> store this temp result
        arr[0] -> arr[0]
        
step2: num = 2:
        compare arr[0] ?= num     2 ?= 2 ----> not missing value

        arr[0] -> arr[1]   ------> move to next item
        k = 4 ----> not change
        result = 1   ---> not change
        
step3: num = 3:
        compare arr[1] ?= num     3 ?= 3 ----> not missing value

        arr[1] -> arr[2]   ------> move to next item
        k = 4 ----> not change
        result = 1   ---> not change
        
step4: num = 4:
        compare arr[2] ?= num     4 ?= 4 ----> not missing value

        arr[2] -> arr[3]   ------> move to next item
        k = 4 ----> not change
        result = 1   ---> not change
        
step5: num = 5:
        compare arr[3] ?= num     7 ?= 5 ----> found one missing value

        arr[3] -> arr[3]
        k -= 1 = 3 ----> found a missing value
        result = num = 5   ---> store the temp result
step6: num = 6:
        compare arr[3] ?= num     7 ?= 6 ----> found one missing value

        arr[3] -> arr[3]
        k -= 1 = 2 ----> found a missing value
        result = num = 6   ---> store the temp result  
step7: num = 7:
        compare arr[3] ?= num     7 ?= 7 

        arr[3] -> arr[4]
        k = 2 ----> not change
        result = 6   ---> not change   
step8: num = 8:
        compare arr[4] ?= num     11 ?= 8

        arr[4] -> arr[4]
        k -= 1 = 1 ----> found one 
        result = 8  ---> update the result
        
step9: num = 9:
        compare arr[4] ?= num     11 ?= 9

        arr[4] -> arr[4]
        k -= 1 = 0 ----> found one 
        result = 9  ---> update the result
"""
### if out of the range of the list?

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # start from the smallest postive interger, then compare each postive integer with the item in the array:
        num = 1
        i = 0
        result = arr[0] - 1
        while k > 0 and i < len(arr):
            if num == arr[i]:
                i += 1
            else:
                k -= 1
                result = num
            num += 1
    # if the missing value is larger than the last item in the array:
        if k > 0 :
            while k > 0:
                k -= 1
                result = num
                num += 1
        return result


 ## Binary Search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # the positvie numbers = 1,2,3,4,5,6,7
        # inpur = [2,3,4,7,11], k = 5
        # if the last number = 11, then expected_end without missing number = 11
        # count(missingNumber) = arr[end] - expected_end
        # 11 - 5 = 6, so total number of missing value is 6, but we are looking for 5th one
        # if count(missingNUmber) > k, then move left/search the left list,
        # if count(missingNumber) < k, search for more missing value from right

        # input = [1,2,3,4], k = 2
        # . count(missingNumber) = 4 -4 = 0, then last number + 2 will be the kth missing value which is 6.

        ## The key is to find a logic to count missing numbers
        left, right = 0, len(arr) - 1
        while left <= right:
            # len <= 1000
            # mid = (left + right) // 2
            mid = left + (right - left) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1

            # left ===> total of existing numbers
            # k is total of missing numbers
        return left + k





