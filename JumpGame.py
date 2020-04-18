__author__ = 'Jie'
from sklearn import preprocessing
"""
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

This is a dynamic programming question. Usually, solving and fully understanding a
dynamic programming problem is a 4 step process:

1)Start with the recursive backtracking solution
2)Optimize by using a memoization table (top-down[2] dynamic programming)
3)Remove the need for recursion (bottom-up dynamic programming)
4)Apply final tricks to reduce the time / memory complexity
All solutions presented below produce the correct result, but they differ in run time and memory requirements.
"""
class Solution:
    def canJump(self, nums) -> bool:
        # solve method one
        n=len(nums)
        if n<2:
            return 0
        reach=0
        i=0
        while i<n and i<=reach:
            reach=max(reach,nums[i]+i)
            if reach>=n-1:
                return True
            i+=1
        return False

    def canJump_1(self,nums):
        #naive method, backtracking. using recursive. O(n2) complexity
        # remember that the recursive problem can be generally replaced by DP method.
        return self.canJumpFromPosition(0,nums)
    def canJumpFromPosition(self,position,nums):
        # this is a help function for canJump_1()
        # this mehtod can be also upgraded, check the nextPoint from right to left.
        n=len(nums)
        if position==n-1:
            return True
        furthestJump=min(nums[position]+position,n-1) # the furthest location it can jump
        nextPosition=position+1
        #nextPosition=furthestJump
        while nextPosition<=furthestJump:
            #while nextPosition>position:
            # the location of next position should be smaller than the furthest jump
            if self.canJumpFromPosition(nextPosition,nums):
                return True
            nextPosition+=1
        return False

    def canJump_2(self,nums):
        #greedy algorithm
        n=len(nums)
        left_most=n-1
        for i in range(n-1,-1,-1):
            if i+nums[i]>=left_most:
                left_most=i
        return left_most==0

solution=Solution()
nums=[3,2,1,0,4]
# ans=solution.canJump(nums)
ans=solution.canJump_1(nums)
print(ans)

