from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        common = count.most_common(k)
        out = []
        for i in common:
            (n, c) = i

            out.append(n)
        
        return out
            