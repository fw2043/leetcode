# prefix sum: 

A prefix sum is a super useful technique that can be used with arrays. Suppose we have an array nums = [2,-1,3,-3,4]. The basic idea here is that we create an array, say, prefix, and fill it up such that the value at its ith index denotes the running sum of a nums subarray that starts from 0 and goes up to and including the ith index. This is extremely useful when we want to retrieve the sum of a subarray ending at an arbitrary index, say i.

So, given an array [2,-1,3,-3,4], the prefix would be [2,1,4,1,5].

After building this sum, we can calculate the sum of any subarray that starts at left and ends at right in O(1) time. This is because we won't need to recalculate it. We can do this by prefix[right] - prefix[left - 1]. 
The -1 will ensure we exclude the running sum of all the numbers before left. However, if left points to 0, 
our prefix[left-1] will just be 0.

    class PrefixSum:
        def __init__(self, nums):
            self.prefix = []
            total = 0
            for n in nums:
                total += n
                self.prefix.append(total)
        
        def rangeSum(self, left, right):
            preRight = self.prefix[right]
            preLeft = self.prefix[left - 1] if left > 0 else 0
            return (preRight - preLeft)



There is another one called postfix which starts from the end of an array, instead of the beginning of an array.

# Time Complexity
The time complexity to build the initial prefix sum is O(n). 
However, to calculate a range sum, we will only perform O(1) operations no matter how big the array is. 
If we don't need the initial array, we can actually overwrite it with its prefix sum, 
which will bring the time complexity to O(1). This works because the size of an array's prefix array will always 
be the same as itself.

# Closing Notes
Prefix sums are ubiquitous and can be extremely useful on integer arrays whenever you need to maintain a running sum. 
It should also be noted that sum is not the only operation we can perform using this technique. 
We can also calculate a prefix product. We can also do the opposite and get a postfix sum, which would do the same operation, 
just in reverse order.