class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        money_memo = [0] * len(nums)
        money_memo[-1] = nums[-1]
        money_memo[-2] = nums[-2]
        money_memo[-3] = nums[-3] + nums[-1]
        for i in range(len(nums)-4, -1, -1):
            money_memo[i] = nums[i] + max(money_memo[i+2], money_memo[i+3])
        
        return max(money_memo[0], money_memo[1])
