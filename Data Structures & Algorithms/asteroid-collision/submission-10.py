class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                s = stack[-1] + a
                if s == 0:
                    stack.pop()
                    a = 0
                elif s > 0:
                    a = 0
                else:
                    stack.pop()
                    

            if a != 0:
                stack.append(a) 

        return stack
        



