class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteriod in asteroids:
            while stack and stack[-1] > 0 and asteriod < 0:
                diff = stack[-1] + asteriod
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    stack.pop()
                    asteriod = 0
                else:
                    asteriod = 0

            if asteriod != 0:
                stack.append(asteriod)
        return stack
                    