class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 1000000
        lp = 0
        rp = 0
        arr_length = len(nums)
        sum = nums[0]
        while (lp <= arr_length-1):
            if sum >= target:
                min_length = min(min_length, rp-lp+1)
                sum -= nums[lp]
                lp += 1
            elif sum < target:
                rp += 1
                if rp == arr_length:
                    break
                sum += nums[rp]
        if min_length == 1000000:
            return 0
        return min_length
        