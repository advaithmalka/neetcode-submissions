class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        preSums = {0:1}
        total = 0
        for num in nums:

            total += num

            if (total - k) in preSums:
                res += preSums[total - k]
                
            preSums[total] = preSums.get(total, 0) + 1


            
        return res