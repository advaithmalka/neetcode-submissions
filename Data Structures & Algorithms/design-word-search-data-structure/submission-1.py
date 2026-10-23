class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.endOfWord

            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
            elif word[i] in curr.children:
                return dfs(i + 1, curr.children[word[i]])

            return False

        return dfs(0, self.root)
