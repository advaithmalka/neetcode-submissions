class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        while len(stones) > 1:
            stones.sort()
            biggest = stones.pop()
            secondBiggest = stones.pop()

            diff = biggest - secondBiggest
            if diff > 0:
                stones.append(diff)
        
        return stones[0] if stones else 0

