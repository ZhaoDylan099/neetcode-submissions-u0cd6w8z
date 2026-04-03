import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        
        nums_modified = [n for n in nums if n != 0]

        if nums_modified:
            product = math.prod(nums_modified)
        else:
            product = 0
        
        if len(nums) - len(nums_modified) >= 2:
            return [0] * len(nums)
        for num in nums:
            if 0 in nums:
                if num != 0:

                    out.append(0)
                else:
                    out.append(product)
            else:
                out.append(product // num)
        return out