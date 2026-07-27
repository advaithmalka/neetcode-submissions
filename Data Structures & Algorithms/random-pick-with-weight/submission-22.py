class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        total = 0
        self.prefixSums = []
        # [1,4]
        for weight in w:
            total += weight
            self.prefixSums.append(total)

    def pickIndex(self) -> int:
        target = random.random() * self.prefixSums[-1]
        # 
        l, r = 0, len(self.prefixSums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if self.prefixSums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()