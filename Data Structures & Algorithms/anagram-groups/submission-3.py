
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        groups = {}


        for s in strs:
            sorted_s = sorted(s)
            k = ''.join(sorted_s)
            
            if k in groups:
                groups[k].append(s)
            
            else:
                groups[k] = [s]

        for _, v in groups.items():

            out.append(v)

        return out