class Solution:
    def reverse(self, x: int) -> int:
        temp = x if x>0 else -x
        divider = 10

        if temp / divider < 1:
            return x
        num = ""
        while temp >= 1:
            num += str(temp%divider)
            temp = temp - (temp%divider)
            temp = temp // divider
        num = int(num)
        if num < -(2**31) or (2**31-1) < num:
            return 0
        if x>0:
            return num
        else:
            return -num