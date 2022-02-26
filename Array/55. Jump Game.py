class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
        
#         if(n == 1): return True
        
#         last = n - 1 
#         for i in reversed(range(0, n-1)):
#             if ( last <= i + nums[i]):
#                 last = i
        
#         return last == 0
        
        
        
        #dp.
        
        """
                                   ::Naive Solution::
        aux(nums, icurr):
            if icurr not ok: false
            if icurr == n-1: return true
            for i in range(icurr+1, icurr + nums[icurr]):
                if aux(nums, i):
                    return true
            return false        
        
        """
        
        """
        aux(nums, icurr, dp):
            if icurr not ok: false
            if icurr == n-1: return true
            
            if dp[icurr]: return true
            for j in range(i+1, i + nums[i]):
                if aux(nums, j, dp) or dp[j]:
                    return true
            
            
        dp = [false]*(n-1) + [true]
        for i in reverse(range(0,n-1)):            
            for j in range(i, math.min( i + nums[i], n)):            
                #dp[i] = aux(nums, j) or dp[i] 
                dp[i] = dp[j] 
                if dp[i]:
                    continue
        
        return dp[0]
        
        ---------------
        n = len(nums)
        dp = [False]*(n-1) + [True]
        for i in reversed(range(0,n-1)):            
            if(nums[i] == 0):
                continue
            for j in range(i+1, min( i + nums[i], n)):            
                if dp[i]: 
                    break
                dp[i] = dp[j] or dp[i]
                
                
        
        return dp[0]
        --------------
       """ 
        n = len(nums)
        dp = [False]*(n-1) + [True]
        for i in reversed(range(0,n-1)):            
            if(nums[i] == 0):
                continue
            for j in range(i+1, min( i + nums[i] + 1, n)):            
                if dp[i]: 
                    break
                dp[i] = dp[j] or dp[i]
                
                
        
        return dp[0]
        
        
    
        