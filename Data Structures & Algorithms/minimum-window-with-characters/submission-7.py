class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""

        tMap = defaultdict(int)
        for char in t:
            tMap[char] += 1

        need = len(tMap)
        have = 0
        sMap = defaultdict(int)
        l = 0
        res = (-1, -1)
        minLen = float("inf")
        for r in range(len(s)):
            c = s[r]
            sMap[c] += 1
            if c in tMap and sMap[c] == tMap[c]:
                have += 1

            while have == need:
                currLen = r - l + 1
                if currLen < minLen:
                    minLen = currLen
                    res = (l, r)
                
                if s[l] in tMap and sMap[s[l]] == tMap[s[l]]:
                    have -= 1
                sMap[s[l]] -= 1
                l+=1

        l, r = res
        return s[l:r + 1] if res[0] != -1 else ""