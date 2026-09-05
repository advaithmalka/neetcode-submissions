class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)
        tMap = defaultdict(int)
        if len(s) != len(t): return False

        for letter in s:
            sMap[letter] = sMap[letter] + 1
        
        for letter in t:
            tMap[letter] = tMap[letter] + 1
        
        return sMap == tMap
