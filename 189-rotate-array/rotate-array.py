class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        lp = 0
        rp = k-1

        while lp < rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
            rp -= 1
        
        lp = k
        rp = len(nums)-1

        while lp < rp:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
            rp -= 1



        