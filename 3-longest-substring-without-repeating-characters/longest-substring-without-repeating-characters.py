class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        
        
        for right in range(len(s)):
            flag = True
            if s[right] in s[left:right]:
                while flag:
                    if s[left] == s[right]:
                        flag = False
                    left += 1
            else:
                maxLen = max(maxLen, right-left+1)
        return maxLen
