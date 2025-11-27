class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s[::-1]
        for char in s:
            if char != " ":
                length += 1
            if length != 0 and char == " ":
                return length
        return length      