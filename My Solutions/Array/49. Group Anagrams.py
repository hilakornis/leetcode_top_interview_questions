class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map with lists.
        # for each one sort it and insert it to the answer.
        # time : O(n)
        # space: O(n)
        
        m = {}
        for i in strs:
            s = "".join(sorted(i))
            if not s in m.keys():
                m[s] = [i]
            else:
                m.get(s).append(i)
        
        res = []
        for ls in m.values():
            res.append(ls)
        return res