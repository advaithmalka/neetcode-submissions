class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket = "({["
        closed_bracket = ")}]"
        for char in s:
            if char in open_bracket:
                if char == "(":
                    stack.append(")")
                elif char == "{":
                    stack.append("}")
                elif char == "[":
                    stack.append("]")
            elif char in closed_bracket:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0