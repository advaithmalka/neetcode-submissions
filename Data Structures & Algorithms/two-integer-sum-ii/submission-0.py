class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptrH = len(numbers) - 1
        ptrL = 0
        while numbers[ptrL] + numbers[ptrH] != target:
            if numbers[ptrL] + numbers[ptrH] < target: ptrL +=1
            elif numbers[ptrL] + numbers[ptrH] > target: ptrH -= 1


        return [ptrL + 1, ptrH + 1]
