class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * (len(nums1))
        numMap = {num:i for i, num in enumerate(nums1)}

        for num in nums2:
            while stack and num > stack[-1]:
                res[numMap[stack.pop()]] = num
            if num in numMap:
                stack.append(num)
        return res
