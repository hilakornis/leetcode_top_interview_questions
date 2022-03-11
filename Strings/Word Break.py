class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        l, r = 0, 1
        out_dict = False
        words = set(wordDict)
        while(r <= len(s) and not out_dict):
            r = l + 1
            not_found = False
            while r <= len(s):                
                if s[l:r] in words:
                    break
                r += 1
                not_found = r > len(s)            
            out_dict = not_found            
            l = r
        
        return not out_dict            
		
		
	 def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        l, r = 0, 1
        out_dict = False
        words = set(wordDict)
        dp = [False for _ in range(len(wordDict) + 1)]
        dp[0] = True
        
        lens = set()
        for w in wordDict:
            lens.add(len(w))
            
        for i in range(len(s)):
            if dp[i]:
                for l in lens:
                    if i+l >= len(s) and dp[min(i+l,len(s)-1)]:
                        return True
                    
                    if s[i, i+l] in words:
                        d[i] = True
        
        
        return False