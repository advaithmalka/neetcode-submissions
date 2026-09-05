class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for s in strs:
            letterFreq = [0] * 26
            for letter in s:
                letterFreq[ord(letter) - ord('a')] += 1
            wordMap[tuple(letterFreq)].append(s)
        return list(wordMap.values())