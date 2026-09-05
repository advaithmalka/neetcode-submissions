class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        total = 0
        res = 0
        for num in nums:
            total += num
            if (total - k) in prefixSums:
                res += prefixSums[(total - k)]
            prefixSums[total] = prefixSums.get(total, 0) + 1

        return res
            

