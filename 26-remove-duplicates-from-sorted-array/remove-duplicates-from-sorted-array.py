class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sample = None
        k = 0
        for i in range(len(nums)):
            if nums[i] != sample:
                sample = nums[i]
                nums[k] = sample
                k += 1
        return k
        