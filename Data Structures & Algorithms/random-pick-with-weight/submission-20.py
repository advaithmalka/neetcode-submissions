class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        total = 0
        self.prefixSums = []
        for weight  in self.w:
            total += weight
            self.prefixSums.append(total)

    def pickIndex(self) -> int:
        randInt = random.random() * self.prefixSums[-1]
        l, r = 0, len(self.prefixSums) - 1
        # [1, 3] R 0
        # 0 1 2 3 
        while l < r:
            mid = (r + l) // 2
            if self.prefixSums[mid] <= randInt:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()