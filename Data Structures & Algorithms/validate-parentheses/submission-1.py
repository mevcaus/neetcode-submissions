class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif not stack:
                return False
            elif c == ")" and stack:
                if stack.pop() != "(":
                    return False
            elif c == "]" and stack:
                if stack.pop() != "[":
                    return False
            elif c == "}" and stack:
                if stack.pop() != "{":
                    return False
        if not stack:
            return True
        return False