class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num in numMap:
            freq[numMap[num]].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            res.extend(freq[i])
            if len(res) == k:
                break
        return res
        # [[], [1], [2], [3]]
