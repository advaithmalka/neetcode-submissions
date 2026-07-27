class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1

        maxL, maxR = height[0], height[-1]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                waterPot = maxL - height[l]
                maxL = max(maxL, height[l])
            else:
                r -= 1
                waterPot = maxR - height[r]
                maxR = max(maxR, height[r])
                
            if waterPot > 0:
                res += waterPot
        return res