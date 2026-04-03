import math

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l],heights[r]) * (r - l)
            if res < area:
                res = area
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            elif heights[r] == heights[l]:
                r -= 1
                l += 1
        return res
                



