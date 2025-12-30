class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if i > 0:
                if nums[i] == 0:
                    maxcount = max(count, maxcount)
                    count = 0
            maxcount = max(count, maxcount)
        return maxcount