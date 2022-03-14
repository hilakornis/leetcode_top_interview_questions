class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + int((r - l) / 2)
            
            if l == r - 1 and nums[l] > nums[r]:
                break
            elif nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid
        return nums[r]