class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        tMap = defaultdict(int)
        window = defaultdict(int)
        for char in t:
            tMap[char] += 1

        l = 0
        need = len(tMap)
        have = 0
        res, resLen = [0,0], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in tMap and window[c] == tMap[c]:
                have += 1

                while have == need:
                    if (r - l + 1) < resLen:
                        resLen = r - l + 1
                        res = [l, r]
                    
                    window[s[l]] -= 1
                    if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                        have -= 1
                    l+=1

        return s[res[0]:res[1] + 1] if resLen != float("inf") else ""