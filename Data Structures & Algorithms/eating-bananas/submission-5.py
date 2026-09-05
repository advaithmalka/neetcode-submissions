class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = max(piles)
        low, high = 1, max(piles)
        while low <= high:
            k = (low + high) // 2
            hours = 0 
            for num in piles:
                hours += math.ceil(num / k)

            if hours <= h:
                minK = min(minK, k)
                high = k - 1
            else:
                low = k + 1
                

        return minK