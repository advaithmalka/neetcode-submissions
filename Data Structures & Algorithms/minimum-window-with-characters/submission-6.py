class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tMap = defaultdict(int)
        for char in t:
            tMap[char] += 1
        
        l = 0
        have = 0
        need = len(tMap)
        sMap = defaultdict(int)
        res = [-1,-1]
        minLen = float("inf")
        for r in range(len(s)):
            sMap[s[r]] += 1
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need and l < len(s):
                if r - l + 1 < minLen:
                    minLen =  r - l + 1
                    res = [l, r]
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        left, right = res
        return s[left:right + 1] if minLen <= len(s) else ""