class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        lp = 0
        rp = 0

        temp = []
        step = 0
        while True:
            # step += 1
            # print("step", step)
            if m == 0:
                for i in range(n):
                    nums1[i] = nums2[i]
                break
            elif n == 0:
                break
            elif lp == m and rp == n:
                for i in range(len(temp)):
                    nums1[i] = temp[i]
                break
            elif lp == m:
                temp.insert(lp+rp,nums2[rp])
                rp += 1
            elif rp == n:
                temp.insert(lp+rp,nums1[lp])
                lp += 1
            elif nums1[lp] >= nums2[rp]:
                temp.insert(lp+rp,nums2[rp])
                rp += 1
            elif nums1[lp] < nums2[rp]:
                temp.insert(lp+rp,nums1[lp])
                lp += 1

        