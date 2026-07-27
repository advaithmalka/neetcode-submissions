class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicates = set()
        unique = {}
        for i, char in enumerate(s):
            if char in unique:
                del unique[char]
                duplicates.add(char)
            elif char not in duplicates:
                unique[char] = i
        return min(unique.values()) if unique else -1