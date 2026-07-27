class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order2Idx = {letter:i for i, letter in enumerate(order)}
        if len(words) == 1:
            return True

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            j = 0
            while j < len(word1) and j < len(word2) and word1[j] == word2[j]:
                j+=1

            if j < len(word1) and j == len(word2) :
                return False

            if j < len(word1) and j < len(word2) and order2Idx[word1[j]] > order2Idx[word2[j]]:
                return False

        return True
