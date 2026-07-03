class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_heights = [0]
        max_height = 0
        total_water = 0
        right_max_height = 0
        for ht in height:
            left_max_heights.append(max(max_height, ht))
            max_height = max(max_height, ht)
        for i in range(len(height) - 1, 0, -1):
            water_added = min(left_max_heights[i], right_max_height) - height[i]
            if water_added > 0:
                total_water += water_added
            right_max_height = max(right_max_height, height[i])
        return total_water
