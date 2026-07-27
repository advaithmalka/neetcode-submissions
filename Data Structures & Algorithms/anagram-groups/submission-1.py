class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =  {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            if str(count) not in res:
                res[str(count)] = []
            res[str(count)].append(s)
        return list(res.values())
                
