class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(stack)
            try: 
                int(token)
                stack.append(token)
            except:
                
                val_1 = int(stack.pop())
                val_2 = int(stack.pop())

                if token == '+':
                    ans = val_1 + val_2
                elif token == '-':
                    ans = val_2 - val_1
                elif token == '*':
                    ans = val_2 * val_1
                elif token == '/':
                    ans = int(val_2 / val_1)
                
                stack.append(ans)
        
        return int(stack[0])


  
