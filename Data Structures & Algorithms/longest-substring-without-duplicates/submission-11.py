class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        longest = 0
        start = 0

        for idx, c in enumerate(s):
            if c in chars and chars[c] >= start:
                start = chars[c] + 1
            
            chars[c] = idx
            longest = max(idx - start + 1, longest)

        return longest
