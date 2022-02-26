class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        #returns k when: [0,k] [k+1, n-1]
        def __findK(nums: List[int]) -> int:
            n = len(nums)
            right = n - 1
            left = 0
                        
            while (left < right):
                mid = left + math.floor((right - left)/2)
                is_rev_mid = nums[mid] > nums[mid+1]
                if is_rev_mid:
                    return mid
                elif nums[mid] > nums[right] : 
                    left = mid
                elif nums[mid] < nums[right] :
                    right = mid - 1
                # elif nums[left] < nums[mid] :
                #     left = mid
                # elif nums[left] > nums[mid] :
                #     right = mid
                            
            return -1
        
        def __binary(nums: List[int], left, right, target: int) -> int:
            if(not left in range(0, len(nums) -1) or (not right in range(0, len(nums) - 1))):
                return -3
            while (left <= right):
                mid = left + math.floor((right - left)/2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else: # nums[mid] > target
                    right = mid - 1
            return -1
                    
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if nums[len(nums) - 1] > nums[0]:
                return __binary(nums, 0, len(nums) - 1, target)            
                
        k = __findK(nums)
        if target in range(nums[0], nums[k]):
            return __binary(nums, 0, k, target)            
        else:
            return __binary(nums,k+1, len(nums)-1, target)
    
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        
        right = len(nums)
        left = 0
        curr = 0
        while(left < right):
            mid = left + math.floor((right - left)/2)
            
            same_side =  (nums[mid] < nums[0]) == (target < nums[0]) 
            if same_side:
                curr  = nums[mid]
            elif target < nums[0]: # target on the right
                curr = (-1) * math.inf
            else: # target is on the left                
                curr = math.inf
            
            if curr == target:
                return mid
            elif curr < target:
                left = mid + 1
            else: # curr > target
                right = mid
                
        return -1