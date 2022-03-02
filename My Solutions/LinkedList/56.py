class Solution:
    """
    class IntervalNode:
        def __init__(self, interval = None:List[int]):
            self.inter = interval
            self.right = None
            self.left = None
        
        def compIntervals(self, i1: List[int], i2: List[int]):
            if i1[1] < i2[0]:
                return -1
            elif i2[1] < i1[0]:
                return 1
            else:
                overlap = (i1[0] < i2[0] and i1[1] in range(i2[0],i2[1])) or 
                          (i1[0] in range(i2[0], i2[1]) and i1[1] in range(i2[0], i2[1])) or 
                          (i2[0] in range(i1[0], i1[1]) and i2[1] in range(i1[0], i1[1])) or 
                          (i2[0] < i1[0] and i2[1] in range(i1[0],i1[1]))
                if overlap:
                    return 0 # min, max to set new val in TreeNode
        def insert(self, interval:List[int]):            
            cmp = self.compIntervals(self.inter, interval)
            if cmp == 0:
            
                  # init an avl tree        
        # each node is with val = start interval, and additional  and represent a non overlapping intervals 
        # when inserting an new interval: (i,j)
            # search for it in each node:
                # check if overlapp. 
                #   no: continue to search or add it as a leaf
                #   yes: update node, and check if the sons are overlapping. 
                #           yes: remove son and update root. and continue checking
                #           no: return
                
        
        
        # inorder treversal through tree and returning a list
       """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
    
        
        return merged
        
        
  