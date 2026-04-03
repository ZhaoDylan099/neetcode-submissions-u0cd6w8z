class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        tracker = {}
        start = 0

        for idx, c in enumerate(s):
        
            if c in tracker:
                start = max(start, tracker[c] + 1)
                
            tracker[c] = idx

            longest = max(idx - start + 1, longest)
            
        return longest