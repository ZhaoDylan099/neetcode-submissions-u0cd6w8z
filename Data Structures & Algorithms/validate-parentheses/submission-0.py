class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            
            if stack and c not in {'{', '[', '('}:
                if c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
    