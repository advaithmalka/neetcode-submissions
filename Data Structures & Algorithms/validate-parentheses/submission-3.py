class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter in "[{(":
                stack.append(letter)
            elif stack and ((letter == "]" and stack[-1] == "[") or 
                 (letter == "}" and stack[-1] == "{") or 
                 (letter == ")" and stack[-1] == "(")):
                stack.pop()
            else: 
                return False
        return len(stack) == 0
