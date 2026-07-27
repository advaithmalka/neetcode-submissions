class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = # of each letter
        wordMap = defaultdict(list)

        for s in strs:
            charFreq = [0] * 26
            for char in s:
                charFreq[ord(char) - ord('a')] += 1
            wordMap[tuple(charFreq)].append(s)
        
        return list(wordMap.values())