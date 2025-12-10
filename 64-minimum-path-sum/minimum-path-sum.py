class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_sum = grid
        if len(min_sum) == 1:
            return sum(min_sum[0])
        
        # last row
        for i in range(len(min_sum[-1])-2, -1, -1):
            min_sum[-1][i] = min_sum[-1][i] + min_sum[-1][i+1]
        
        # last column
        for i in range(len(min_sum)-2, -1, -1):
            min_sum[i][-1] = min_sum[i][-1] + min_sum[i+1][-1]
        
        # rest of the grid
        for i in range(len(min_sum)-2, -1, -1):
            for j in range(len(min_sum[-1])-2, -1, -1):
                min_sum[i][j] = min_sum[i][j] + min(min_sum[i+1][j], min_sum[i][j+1])
        
        return min_sum[0][0]

            

        