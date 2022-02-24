class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        count_dup = 0
        last_org_num = -1010 #last_original_num
        pos_out_range = 10100
        dup_to_fill = pos_out_range
        # mark duplicates places in the array and remove them
        for i in range(len(nums)):                        
            is_dup = nums[i] == last_org_num
            if not is_dup:
                last_org_num = nums[i]
                exist_dup = dup_to_fill != pos_out_range
                if exist_dup:
                    nums[dup_to_fill] = nums[i]
                    dup_to_fill = min(i, dup_to_fill+1)                    
                
            else:
                count_dup += 1                
                dup_to_fill = min(i, dup_to_fill)
                      
        
        return dup_to_fill           