class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            start_index = i

            while stack and h < stack[-1][1]:
                popped_index, popped_height = stack.pop()
                max_area = max(max_area, popped_height * (i - popped_index))
                start_index = popped_index
            stack.append([start_index, h])
        for i,h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area