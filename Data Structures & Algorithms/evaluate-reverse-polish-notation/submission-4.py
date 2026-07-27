class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        ops = ["*", "/", "+", "-"]
        for i in range(len(tokens)):
            if tokens[i] in ops:
                if tokens[i] == "+":
                    numbers[-2] += numbers[-1]
                elif tokens[i] == "*":
                    numbers[-2] *= numbers[-1]
                elif tokens[i] == "-":
                    numbers[-2] -= numbers[-1]
                elif tokens[i] == "/":
                    numbers[-2] = int(numbers[-2] / numbers[-1])
                numbers.pop()
                print(numbers)
            else: numbers.append(int(tokens[i]))
        

        return numbers[-1]
