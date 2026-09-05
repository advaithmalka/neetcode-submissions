class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums) + 1)]
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1
        
        for num, freq in numMap.items():
            freqList[freq].append(num)

        res = []
        for i in range(len(freqList) - 1, -1, -1):
            res.extend(freqList[i])
            if len(res) >= k:
                return res

