class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = maxProd = minProd = nums[0]
        for n in nums[1:]:
            candidates = [n, maxProd*n, minProd*n]
            maxProd = max(candidates)
            minProd = min(candidates)
            output = max(output, maxProd)
        return output