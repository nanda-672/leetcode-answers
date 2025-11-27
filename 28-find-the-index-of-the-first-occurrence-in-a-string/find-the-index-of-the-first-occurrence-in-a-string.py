class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size = len(needle)
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)-needle_size+1):
                if haystack[i:i+needle_size] == needle:
                    return i

        