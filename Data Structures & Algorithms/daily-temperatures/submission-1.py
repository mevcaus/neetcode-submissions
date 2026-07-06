class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for index in range(len(temperatures) - 1, -1, -1):
            current_temp = temperatures[index]
            if not stack:
                stack.append(index)
                res.append(0)
                continue
            while stack and current_temp >= temperatures[stack[-1]]:
                stack.pop()
            if stack and current_temp > temperatures[stack[-1]]:
                res.append(0)
            elif stack:
                res.append(stack[-1] - index)
            else:
                res.append(0)
            stack.append(index)
        res.reverse()
        return res
            