class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.prefixSums = [0]
        for num in nums:
            total += num
            self.prefixSums.append(total)


    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSums[right + 1] - self.prefixSums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)