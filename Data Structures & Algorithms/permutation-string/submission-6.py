class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = defaultdict(int)
        for char in s1:
            need[char] += 1
        
        l = 0
        have = defaultdict(int)
        for i in range(len(s1)):
            have[s2[i]] += 1

        for r in range(len(s1), len(s2)):
            if need == have:
                return True

            have[s2[r]] += 1
            have[s2[l]] -= 1
            if have[s2[l]] == 0:
                del have[s2[l]]
            l+=1

        
        return have == need

            