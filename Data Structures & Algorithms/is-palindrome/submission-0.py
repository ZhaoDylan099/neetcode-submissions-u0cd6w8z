class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        modified = "".join(c for c in s if c.isalnum())
        front = 0
        back = len(modified) - 1
        while front < back:

            if modified[front] != modified[back]:
                return False
            front += 1
            back -= 1

        return True        