class Solution:
    memo ={
        0 : [1],
        1 : [1,1]
    }
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in self.memo:
            return self.memo[rowIndex]
        else:
            for i in range(rowIndex+1):
                if i in self.memo:
                    pass
                else:
                    ith_arr = [1]
                    prev_arr = self.memo[i-1]
                    for j in range(i-1):
                        ith_arr.append(prev_arr[j]+prev_arr[j+1])
                    ith_arr.append(1)
                    self.memo[i] = ith_arr
            return self.memo[rowIndex]

        