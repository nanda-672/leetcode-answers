class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        arr_length = len(s)
        if arr_length == 0:
            return True
        lp = 0
        rp = arr_length-1
        while lp < rp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1
        return True
        