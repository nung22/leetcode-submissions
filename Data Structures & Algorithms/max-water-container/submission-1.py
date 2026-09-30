class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            result = max(result, height * width)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return result