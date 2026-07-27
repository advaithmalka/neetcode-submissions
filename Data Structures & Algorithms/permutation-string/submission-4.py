class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1map = defaultdict(int)
        for letter in s1:
            s1map[letter] += 1

        s2map = defaultdict(int)
        for i in range(len(s1)):
            s2map[s2[i]] += 1
        if s1map == s2map: return True 
        for i in range(len(s2) - len(s1)):
            s2map[s2[i+len(s1)]] += 1
            if s2map[s2[i]] == 1: del s2map[s2[i]]
            else:  s2map[s2[i]] -= 1

            if s1map == s2map: return True 

        return False