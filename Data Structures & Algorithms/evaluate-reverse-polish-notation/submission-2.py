class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+": lambda a,b: a + b, "-": lambda a,b: a - b, "*": lambda a,b: a*b, "/": lambda a,b: int(a/b)}
        stack = []
        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operators[token](operand1, operand2))
            else:
                stack.append(int(token))
        return stack.pop()