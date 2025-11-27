class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height)-1
        area = 0

        while True:
            temp = min(height[lp],height[rp])*(rp-lp)
            if temp >= area:
                area = temp
            
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
            
            if lp == rp:
                break
        
        return area