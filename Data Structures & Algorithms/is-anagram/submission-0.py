class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTable = {}
        for letter in s:
            currentCount = sTable.get(letter, 0)
            sTable[letter] = currentCount + 1

        tTable = {}
        for letter in t:
            currentCount = tTable.get(letter, 0)
            tTable[letter] = currentCount + 1

        return sTable == tTable