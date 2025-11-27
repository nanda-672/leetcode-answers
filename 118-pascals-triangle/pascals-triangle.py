class Solution:
    memo = {
        0 : [1],
        1 : [1,1]
    }
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            if i in self.memo:
                pascal.append(self.memo[i])
            else:
                ith_arr = [1]
                prev_arr = pascal[-1]
                for j in range(i-1):
                    ith_arr.append(prev_arr[j]+prev_arr[j+1])
                ith_arr.append(1)
                pascal.append(ith_arr)
                self.memo[i] = ith_arr
        return pascal

        