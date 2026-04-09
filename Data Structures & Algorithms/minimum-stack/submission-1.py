class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = 2**31 - 1
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_val:
            self.min_val = val
            self.history.append(val)


    def pop(self) -> None:
        
        if self.min_val == self.stack[-1]:
            del self.history[-1]
            if self.history:
                self.min_val = self.history[-1]
            else:
                self.min_val = 2**31 - 1
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
        
