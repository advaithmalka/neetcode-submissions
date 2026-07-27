class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(substr):
            l,r = 0, len(substr) - 1
            while l <= r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
            return True
        subres = []
        def dfs(i):
            if i >= len(s):
                res.append(subres.copy())

            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    subres.append(s[i:j+1])
                    dfs(j+1)
                    subres.pop() # restore 
        
        dfs(0)
        return res