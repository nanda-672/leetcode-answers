class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_table = [100000] * len(nums)
        jump_table[-1] = 0
        n = len(nums)
        for i in range(n-2, -1, -1):
            # print(nums[i] + i)
            if nums[i] + i >= n-1:
                jump_table[i] = 1
            else:
                # print("bawah")
                min_jump = 100000
                for j in range(nums[i]+1):
                    if i + j < n:
                        if jump_table[i+j] + 1 < min_jump:
                            min_jump = jump_table[i+j] + 1
                jump_table[i] = min_jump
        
        # print(jump_table)
        return jump_table[0]



            

        