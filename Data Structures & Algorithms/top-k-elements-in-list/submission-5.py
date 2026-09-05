class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1
        
        freqMap = defaultdict(list)
        for num,freq in numMap.items():
            freqMap[freq].append(num)

        freqList = list(freqMap.keys())
        heap = [-f for f in freqList]
        heapq.heapify(heap)

        res = []
        while len(res) < k and heap:
            freq = heapq.heappop(heap) * -1
            res.extend(freqMap[freq])
        return res[:k]
