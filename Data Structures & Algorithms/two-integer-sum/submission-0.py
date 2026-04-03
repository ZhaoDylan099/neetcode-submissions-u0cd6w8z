class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        di = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in di:
                return [di[diff], i]
            
            else:
                di[nums[i]] = i

        return None 