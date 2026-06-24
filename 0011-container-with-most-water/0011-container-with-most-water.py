class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current width and current height
            width = right - left
            current_height = min(height[left], height[right])
            
            # Calculate current area and update max_water if it's larger
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water