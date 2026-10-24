class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.endOfWord = True
        
        res = []
        def dfs(r, c, curr, word):
            if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or 
                board[r][c] not in curr.children):
                return

            char = board[r][c]
            curr = curr.children[char]
            word += char
            if curr.endOfWord:
                res.append(word)
                curr.endOfWord = False
            board[r][c] = "#"

            dfs(r + 1, c, curr, word)
            dfs(r - 1, c, curr, word) 
            dfs(r, c + 1, curr, word)
            dfs(r, c - 1, curr, word)
            board[r][c] = char


        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c, root, "")
        return res
