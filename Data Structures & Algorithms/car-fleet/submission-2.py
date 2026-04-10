class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        data = dict(zip(position,speed))

        sorted_position = sorted(position)

        stack = []

        for p in sorted_position:

            while stack and ((target-stack[-1])/data[stack[-1]]) <= ((target-p)/data[p]):

                stack.pop()
            
            stack.append(p)
        

        return len(stack)