__author__ = 'Jie'
"""
45. Jump Game II
Hard

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:
You can assume that you can always reach the last index.
"""

class Solution:
    def jump(self, nums) -> int:
        # first exceptions
        if nums is None or len(nums)<=1:
            return 0
        ## step is the jump step,
        #currentMax is the maximum index at the current step
        # nextMax is the maximum index at the next step in current calculation.
        n=len(nums)
        step,currentMax,nextMax=0,0,0
        i=0
        while i<=currentMax:
            while i<=currentMax:
                nextMax=max(nextMax,i+nums[i])
                i+=1
            currentMax=nextMax
            step+=1
            if currentMax>=n-1:
                return step
        return 0
solution=Solution()
nums=[2,3,1,1,4]
ans=solution.jump(nums)
print (ans)

