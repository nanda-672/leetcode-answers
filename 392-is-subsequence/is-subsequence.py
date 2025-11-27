class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_p = 0
        s_length = len(s)
        t_length = len(t)

        if s_length == 0:
            return True

        if t_length == 0:
            return False

        for char in t:
            if char == s[s_p]:
                s_p += 1
            if s_p == s_length:
                return True
        return False
            
        