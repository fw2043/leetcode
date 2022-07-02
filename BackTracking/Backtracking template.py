"""
https://blog.csdn.net/crystal6918/article/details/51924665
leetcode解题笔记：backtracking类型解题思路
"""
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate) # if it is the list, you need to pop, like leetcode 22, stack.pop()

# combination, permutation(all subsets problems)
# The different between combination and permutation is for combination, k is not changale, for permutation k is changable
# decision tree(left childen, right childen), how to dedup computation, like leetcode 90 and 39

# permutations: leetcode 46, 47
"""
递归函数的开头写好跳出条件，满足条件才将当前结果加入总结果中
已经拿过的数不再拿 if(s.contains(num)){continue;}
遍历过当前节点后，为了回溯到上一步，要去掉已经加入到结果list中的当前节点。
"""
# subsets: leetcode 78, 90
"""
Subsets问题，是取一个数组的组合而不是全排列，基本代码结构都很相似，不同的有：
不是在结果长度等于数组长度时才将结果加入总结果中，而是在每次递归中都将当前组合加入结果中，因为求的是子集而不是全排列。
每次递归不是在池子中随便取一个数加入当前结果，因为此题要求的是子集，[1,3]和[3,1]是相同的，要求的是[1,3]，
因此每次在取数时，都要从其位置开始取后面的数，防止取到[3,1]这样的结果。
"""
# Combination Sum
"""
Combination Sum其实求的是一个subsets问题，在给定的数组中任意取几个数和为最后的target，这其中一个数可以被重复取。
因此大致思路和subsets问题一致;
而Combination Sum II则是每个数只能取一次，这就和最原始的题一样，那么pos递归传递的就是pos+1；第二个不同是数组中可能有重复的数，那就参照上面的follow-up将原始数组排序并维护一个visited辅助数组。

Combination Sum III则是1-9中任取k个数和为n，是原始的subsets问题加上一些限制条件而已。
"""

# Difference bwtween backtracking and dfs?
