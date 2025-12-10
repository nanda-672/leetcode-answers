class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        min_sum = [[] for i in range(len(triangle))]
        min_sum[-1] = triangle[-1]
        min_sum[0] = triangle[0]
        for i in range(len(triangle)-2, 0, -1):
            for j in range(len(triangle[i])):
                min_sum[i].append(min(min_sum[i+1][j], min_sum[i+1][j+1]) + triangle[i][j])

        return min(min_sum[1][0], min_sum[1][1]) + min_sum[0][0]
        