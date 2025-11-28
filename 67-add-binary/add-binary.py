class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        if len(a) < len (b):
            a, b = b, a
        ans = ""
        carry = 0
        for i in range(len(a)):
            a_num = int(a[i])
            if i < len(b):
                b_num = int(b[i])
            else:
                b_num = 0
            if a_num + b_num + carry == 3:
                ans += '1'
                carry = 1
            elif a_num + b_num + carry == 2:
                ans += '0'
                carry = 1
            elif a_num + b_num + carry == 1:
                ans += '1'
                carry = 0
            else:
                ans += '0'
                carry = 0
        if carry == 1:
            ans += '1'
        return ans[::-1]
