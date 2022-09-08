class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        
        maxLen = 0
        for i in range(len(s)-1): # i is starting point
            if (len(s)-i < maxLen): # can't be a longer substring if there aren't enough characters left
                return maxLen
            
            for j in range(i+1, len(s)): # loop through from starting point
                if (s[j] in s[i:j]): # repetition
                    maxLen = max(maxLen, j-i) # update maxLen
                    break
            
            else: maxLen = max(maxLen, j-i+1) # update maxLen
            
        return maxLen
