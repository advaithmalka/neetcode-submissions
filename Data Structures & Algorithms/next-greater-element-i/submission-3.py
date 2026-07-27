class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        res = [-1, 3, -1]
        nums1 map = {4: 0, 1: 1, 2: 2}
        stack = [4, 2]
        find next greater of stack[-1]
        append to stack if num in nums1
        """
        nums1ToIdx = {}
        for i, num in enumerate(nums1):
            nums1ToIdx[num] = i

        stack = []
        res = [-1] * len(nums1)
        for num in nums2:
            while stack and num > stack[-1]:
                idx = nums1ToIdx[stack.pop()]
                res[idx] = num
            if num in nums1ToIdx:
                stack.append(num)
        return res