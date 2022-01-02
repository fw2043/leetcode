"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        # input:  s = "aaab"
        count = Counter(s)  # hashmap: {'a': 3, 'b': 1}
        # maxHeap: {[-3,'a'], [-1, 'b']}, put [-3,'a'], instead of ['a', 3] for sorting purpose and also max: * -1
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ''
        while maxHeap or prev:  # either means there is still more characters need to add
            if prev and not maxHeap:  # if there is still more left, means it is not possible
                return ''
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # it is negative,so instead of minusing 1, we need to add 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]

        return res