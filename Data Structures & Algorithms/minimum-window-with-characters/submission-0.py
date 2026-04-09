from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0

        freq = dict(Counter(t))
        w = defaultdict(int)

        length = len(s) + 1
        res = ""
        valid = False
        for i in range(len(s)):
            if s[i] in freq:
                w[s[i]] += 1
            
            if len(w) != len(freq):
                valid = False
            
            else:
                for k,v in w.items():
                    if v < freq[k]:
                        valid = False
                        break
                    else:
                        valid = True
            
            while valid:

                if len(s[l:i+1]) < length:
                    length = len(s[l:i+1])
                    res = s[l:i+1]
                
                if s[l] in freq:
                    w[s[l]] -= 1
                    if w[s[l]] < freq[s[l]]:
                        valid = False
                l += 1

        return res
        

