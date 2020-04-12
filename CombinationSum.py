__author__ = 'Jie'
"""
39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution:
    def combinationSum(self, nums, target: int):
        # recursion method, it is a classic combination problem.
        self.result=[]
        def help_recur(nums,tmp, remainder, index):
            # tmp is a list
            if remainder==0:
                self.result.append(tmp[:])
                return
            if remainder<-1:
                return
            for i in range(index,len(nums)):
                tmp.append(nums[i])
                help_recur(nums,tmp,remainder-nums[i],i)
                tmp.pop()
        help_recur(nums,[],target,0)
        return self.result

solution=Solution()
nums = [2,3,6,7]
target = 7
ans=solution.combinationSum(nums,target)
print (ans)



