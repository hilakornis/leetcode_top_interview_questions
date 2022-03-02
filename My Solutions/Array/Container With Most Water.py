class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        MAX = 0
        area = 0
        while(left != right):
            if height[left] <= height[right]:
                area = height[left] *( right - left)
                left += 1
            else: # height[left] > height[right]
                area = height[right] * (right - left)
                right -= 1
            MAX = max(MAX, area)
        return MAX