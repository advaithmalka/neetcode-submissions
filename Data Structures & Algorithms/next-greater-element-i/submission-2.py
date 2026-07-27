class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        numMap = {}
        for i, num in enumerate(nums1):
            numMap[num] = i
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                res[numMap[stack.pop()]] = num
            if num in numMap:
                stack.append(num)


        return res