class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = ""
        for i in range(-1,-len(x)-1,-1):
            reverse += str(x[i])
        if x == reverse:
            return True
        else:
            return False
        