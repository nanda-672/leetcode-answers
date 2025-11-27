class Solution:
    memo = {
        0 : 0,
        1 : 1,
        2 : 1
    }
    def countBits(self, n: int) -> List[int]:
        bit_list = []
        range_start = 2
        for i in range(n+1):
            if i in self.memo:
                bit_list.append(self.memo[i])
            else:
                while range_start*2 <= i:
                    range_start *= 2
                if range_start*2 == i:
                    range_start *= 2
                    self.memo[i] = 1
                    bit_list.append(1)
                else:
                    b = self.memo[i-range_start]
                    self.memo[i] = 1 + b
                    bit_list.append(self.memo[i])
        return bit_list
                