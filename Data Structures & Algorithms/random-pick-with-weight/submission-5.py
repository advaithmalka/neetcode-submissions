class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0]
        for weight in w:
            self.prefix.append(weight + self.prefix[-1])

        # [0, 1, 4]

    def pickIndex(self) -> int:
        randInt = random.random() * self.prefix[-1]
        # find closest number to randint
        l, r = 1, len(self.prefix)
        while l < r:
            mid = (l + r) // 2
            if self.prefix[mid] < randInt:
                l = mid + 1
            else:
                r = mid

        return l - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()