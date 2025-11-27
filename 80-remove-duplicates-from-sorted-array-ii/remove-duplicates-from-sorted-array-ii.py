class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        sample = None
        count = 0
        for i in range(len(nums)):
            if nums[i] != sample:
                sample = nums[i]
                nums[k] = sample
                k += 1
                count = 1
            elif nums[i] == sample and count < 2:
                nums[k] = sample
                k += 1
                count += 1
        return k