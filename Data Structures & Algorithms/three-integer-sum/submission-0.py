class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
        
        res = set()
        value_record = set()
        for k, target in enumerate(nums):
            record = set()
            
            for i, num in enumerate(nums):
                
                if i != k:
                    
                    diff = -target - num
                    if diff in record and frozenset([num,diff,target]) not in value_record:
                        res.add((num, diff, target))
                        value_record.add(frozenset([num,diff,target]))
                    else:
                        record.add(num)

        out = [list(r) for r in res]
        return out
                    
