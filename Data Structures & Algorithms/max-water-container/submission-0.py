class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while(left < right):
            if heights[left] < heights[right]:
                currHeight = heights[left] 
            else: 
                currHeight = heights[right]
            currWidth = right - left
            currArea = currHeight * currWidth

            if currArea > maxArea:
                maxArea = currArea
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea
