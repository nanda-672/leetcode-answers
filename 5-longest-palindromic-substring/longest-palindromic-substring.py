class Solution:
    memo = {}
    def isPalindrome(self, s: str):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left:right+1] in self.memo:
                self.memo[s] = True
                return True
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        self.memo[s] = True
        return True
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        palindrome = ""
        for lp in range(len(s)):
            for rp in range(lp, len(s)):
                sample = s[lp:rp+1]
                if rp-lp+1 <= len(palindrome):
                    pass
                # if self.isPalindrome(sample):
                if sample == sample[::-1]:
                    if rp-lp+1 > len(palindrome):
                        palindrome = sample
        return palindrome
                    
        # lp = 0
        # rp = 1
        # palindrome = ""
        # while True:
        #     if lp == len(s)-1:
        #         break
        #     sample = s[lp:rp]
        #     if sample == sample[::-1]:
        #         if rp-lp > len(palindrome):
        #             palindrome = sample
        #         rp += 1
        #     else:
        #         lp += 1
        # return palindrome
