from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        l = 0
        r = l + len(s1) - 1

        freq = dict(Counter(s1))
        w_freq = defaultdict(int)

        
        for i in range(len(s2)):
            
            w_freq[s2[i]] += 1

            if i > len(s1) - 1:
                w_freq[s2[i - len(s1)]] -= 1

                if w_freq[s2[i - len(s1)]] == 0:
                    del w_freq[s2[i - len(s1)]]
       
            if w_freq == freq:
                return True

            
            
        return False
            