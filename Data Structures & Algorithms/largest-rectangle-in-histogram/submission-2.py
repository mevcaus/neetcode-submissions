class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            start_index = index

            while stack and height < stack[-1][1]:
                popped_index, popped_height = stack.pop()
                max_area = max(max_area, popped_height * (index - popped_index))
                start_index = popped_index
            stack.append([start_index, height])
        
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        return max_area