class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap  = {}
        for n in nums:
            numMap[n] = numMap.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)] #  [[][][][][][]]

        for num, count in numMap.items():
            freq[count].append(num)

        res = []
        i = 1
        while len(res) != k:
            res.extend(freq[len(freq) - i])
            i+=1

        return res
        
