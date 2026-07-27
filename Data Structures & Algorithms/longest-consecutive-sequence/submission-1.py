class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)
        for num in nums:
            setLen = 0
            if num - 1 not in numSet: # constant time operation
                setLen = 1
                tempNum = num
                while tempNum + 1 in numSet: 
                    setLen +=1
                    tempNum +=1
                if setLen > maxLen: maxLen = setLen

        return maxLen
