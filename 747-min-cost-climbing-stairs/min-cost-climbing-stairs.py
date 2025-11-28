class Solution:
    # memo = {}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len(cost) == 2:
        #     return min(cost[0],cost[1])
        # elif len(cost) < 2:
        #     return 0
        # # elif len(cost) in self.memo:
        # #     return self.memo[len(cost)]
        # answer = self.minIgnoreNone(self.minCostClimbingStairs(cost[:-1])+cost[-1], self.minCostClimbingStairs(cost[:-2])+cost[-2])
        # # self.memo[len(cost)] = answer
        # return answer

        dp = [0] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        
        return min(dp[0], dp[1])
        
