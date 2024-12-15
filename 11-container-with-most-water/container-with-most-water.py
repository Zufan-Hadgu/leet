class Solution:
    def maxArea(self, height: List[int]) -> int:
        water_amt = 0
        left = 0 
        right = len(height) - 1
        while  left < right:
            water = min(height[left],height[right]) * (right - left)
            water_amt = max(water_amt,water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water_amt
        
        