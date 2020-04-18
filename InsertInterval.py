__author__ = 'Jie'
"""
57. Insert Interval
Hard
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""
# Define an interval
# class Interval():
#     def __init__(self,s=0,e=0):
#         self.start=s
#         self.end=e

class Solution:
    def insert(self, intervals, newInterval):
        # method 1, just append the newInerval, and then call the function merge.
        intervals.append(newInterval)
        return self.merge(intervals)

    def insert_2(self,intervals,newInterval):
        # this method is to find the overlapping set, and merge that range
        # output = left +merged (overlappings) +right
        # time complexity is O(n)
        n=len(intervals)
        new_start,new_end=newInterval
        left,right=[],[]
        for i in range (n):
            if new_start>intervals[i][1]:
                left.append(intervals[i])
            elif new_end<intervals[i][0]:
                right.append(intervals[i])
            else:
                #### noted: the new_start should be updated all the time
                new_start=min(intervals[i][0],new_start)
                new_end=max(intervals[i][1],new_end)

        return left+[[new_start,new_end]]+right

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
intervals = [[1,3],[6,9]]
newInterval = [2,5]
# ans=solution.insert(intervals,newInterval)
ans=solution.insert_2(intervals,newInterval)
print (ans)


