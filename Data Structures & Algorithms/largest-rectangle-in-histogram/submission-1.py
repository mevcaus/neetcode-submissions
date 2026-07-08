class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for curr_index, curr_height in enumerate(heights):
            start_index = curr_index

            while stack and stack[-1][1] > curr_height:
                popped_index, popped_height = stack.pop()
                max_area = max(max_area, popped_height * (curr_index - popped_index))
                start_index = popped_index
            stack.append([start_index, curr_height])
            
        
        for index, height in stack:
            max_area = max(max_area, (len(heights) - index) * height)
        return max_area
