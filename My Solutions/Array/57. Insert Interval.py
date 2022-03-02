class Solution:    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert it to sorted intervals. by newInterval[0]
        # merged overlapping as I did last question
        # return it
        n = len(intervals)
        inserted = False
        
        if n == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                        
        return merged