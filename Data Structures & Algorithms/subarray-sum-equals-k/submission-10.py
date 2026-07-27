class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numMap = {0:1}
        total = 0
        res = 0
        for num in nums:
            total += num
            if total - k in numMap:
                res += numMap[total - k]
            numMap[total] = numMap.get(total, 0) + 1
        return res
        # {}