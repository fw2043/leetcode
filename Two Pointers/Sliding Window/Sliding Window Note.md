# **Sliding Window**
1. Basic idea: https://www.geeksforgeeks.org/window-sliding-technique/
2. Time complxity: Linear 
# Intuition:
    In any sliding window based problem we have two pointers. 
    One right pointer whose job is to expand the current window 
    and then at a point, the window becomes invalid, 
    then we have the left pointer whose job is to contract a given window until it becomes valid again
    At any point in time only one of these pointers move and the other one remains fixed.
#Pattern:
1. 定义需要用到的变量，

    如快慢指针int slow = 0, int fast = 0; 
    
    输入的string s; 
    
    Hashmap char_freq 用于记录string s当中slow到fast（包含）之间所有的字母出现的频率；
    
    int longest记录符合题目要求的最长substring长度等

2. 定义双while循环

        while fast < len(s)：
        
            char_freq[s[fast]] = char_freq.get(s[fast], 0) + 1
            ......
            ......
            while 符合slow指针移动的条件:
                char_freq[s[slow]] -= 1
                ......
                ......
                slow += 1
            if/while 符合某些判断条件:
                longest = max(longest, fast - slow + 1)
            fast += 1
        return longest

3. Youtube expalination: https://www.youtube.com/watch?v=nKhteIRZ2Ok
