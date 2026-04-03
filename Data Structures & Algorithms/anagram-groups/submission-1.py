
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}


        for s in strs:
            sorted_s = sorted(s)
            k = ''.join(sorted_s)
            
            if k in groups:
                groups[k].append(s)
            
            else:
                groups[k] = [s]

        return list(groups.values())