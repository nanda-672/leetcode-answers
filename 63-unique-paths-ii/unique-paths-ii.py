class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        unique_path = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        
        if obstacleGrid[-1][-1] == 1:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        # last row
        for i in range(len(unique_path[-1])-1 , -1, -1):
            if obstacleGrid[-1][i] == 1:
                for j in range(i):
                    unique_path[-1][j] = 0
                break
            else:
                unique_path[-1][i] = 1

        # last column
        for i in range(len(unique_path)-1 , -1, -1):
            if obstacleGrid[i][-1] == 1:
                for j in range(i):
                    unique_path[j][-1] = 0
                break
            else:
                unique_path[i][-1] = 1
        
        for i in range(len(unique_path)-2, -1, -1):
            for j in range(len(unique_path[i])-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    unique_path[i][j] = 0
                else:
                    unique_path[i][j] = unique_path[i+1][j] + unique_path[i][j+1]

        print(unique_path)
        return unique_path[0][0]



        