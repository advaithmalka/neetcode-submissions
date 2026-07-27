class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {1 : 1, 2: 2, 3: 3}
        # [[], [1],[2],[3]]
        freq = [[] for _ in range(len(nums) + 1)]
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1

        for num in hashMap:
            freq[hashMap[num]].append(num)
        
        res = []
        i = len(freq) - 1
        while len(res) < k:
            if freq[i]:
                res.extend(freq[i])
            i -= 1

        return res
       

        