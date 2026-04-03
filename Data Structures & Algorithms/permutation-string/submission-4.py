from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        l = 0
        r = l + len(s1) - 1

        freq = dict(Counter(s1))

        while r < len(s2):
            
            w_freq = dict(Counter(s2[l:r + 1]))

            if w_freq == freq:
                return True
            l += 1
            r += 1
        return False
            