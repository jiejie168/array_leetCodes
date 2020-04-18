__author__ = 'Jie'
"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
class Solution:
    def merge(self, intervals):
        # sort and loop
        n=len(intervals)
        intervals.sort(key=lambda x: x[0])
        result=[]
        i=0
        while i<n:
            cur_start,cur_end=intervals[i]
            if result:
                pre_start,pre_end=result[-1]
                lo=max(pre_start,cur_start)
                hi=min(pre_end,cur_end)
                if hi>=lo:
                    if cur_end>pre_end:
                        result[-1]=[pre_start,cur_end]
                else:
                    result.append(intervals[i])
            else:
                result.append(intervals[i])
            i+=1
        return result



solution=Solution()
# intervals=[[1,3],[2,6],[8,10],[15,18]]
intervals=[[1,4],[2,3]]
ans=solution.merge(intervals)
print (ans)


