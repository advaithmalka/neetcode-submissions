class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                prevTemp, prevIdx = stack.pop()
                res[prevIdx] = idx - prevIdx
            stack.append((temperature, idx))
        return res