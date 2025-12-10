class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [-(10**4)] * len(nums)
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            memo[i] = nums[i] + max(0, memo[i-1])
        
        return max(memo)

        