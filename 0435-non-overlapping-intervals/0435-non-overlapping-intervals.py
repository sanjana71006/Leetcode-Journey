class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[0]))
        count=0 
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>intervals[i+1][0]:
                count+=1 
                intervals.pop(i+1)
            else:
                i+=1 
        return count
