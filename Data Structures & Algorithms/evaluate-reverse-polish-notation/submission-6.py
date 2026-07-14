class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a,b: a + b, 
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: int(a / b),
        }
        for token in tokens:
            if token in operations:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operations[token](operand1, operand2))
            else:
                stack.append(int(token))
        return stack[0]