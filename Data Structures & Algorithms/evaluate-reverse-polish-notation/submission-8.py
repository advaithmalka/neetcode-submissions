class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []
        for token in tokens:
            if token in operators:
                n = stack.pop()
                if token == "+":
                    stack[-1] += n
                elif token == "-":
                    stack[-1] -= n
                elif token == "*":
                    stack[-1] *= n
                else:
                    stack[-1] = int(stack[-1] / n)
            else:
                stack.append(int(token))
        return stack[-1]