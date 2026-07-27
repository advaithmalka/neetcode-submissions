class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            x = hashmap.get(target - n, None)
            if x is not None:
                return [x, i]
            hashmap[n] = i

            