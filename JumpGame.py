__author__ = 'Jie'
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

solution=Solution()
nums=[3,2,1,0,4]
ans=solution.canJump(nums)
print(ans)
