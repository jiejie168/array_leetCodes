__author__ = 'Jie'
"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Solution:
    def combinationSum2_1(self, nums, target: int):
        # DFS, recursion, depth-first search
        n=len(nums)
        nums.sort()
        self.result=set() # remove the duplicate iterm by set()

        def dfs(nums,tmp,remainder, index):
            # tmp is the temparary list
            if remainder==0:
                # this is the end of recursion
                self.result.add(tuple(tmp[:])) # list should be first changed to tuple, so that it can be added by set
                return
            if remainder<=-1:
                return
            for i in range(index,n):
                tmp.append(nums[i])
                dfs(nums,tmp,remainder-nums[i],i+1)  # recursion relation, i should increase to avoid duplicate element
                tmp.pop()

        dfs(nums,[],target,0)
        return [list(i) for i in self.result]


    def combinationSum2_2(self, nums, target):
        nums.sort()
        res=set()
        self.dfs(nums,target,0,[],res)
        return [list(i) for i in res]

    def dfs(self,nums,remainder,index,tmp,res):
        # res: the final result set
        # tmp: the temporay list
        if remainder==0:
            res.add(tuple(tmp[:]))
            return
        if remainder<0:
            return
        for i in range(index,len(nums)):
            if remainder<nums[i]: return
            tmp.append(nums[i])
            self.dfs(nums,remainder-nums[i],i+1,tmp,res)
            tmp.pop()

nums=[10,1,2,7,6,1,5]
target = 8
solution=Solution()
# ans=solution.combinationSum2_1(nums,target)
ans=solution.combinationSum2_2(nums,target)
print (ans)






# aa=set()
# nums=[[1,2],[2,1],[1,3],[3,1]]
# for i in nums:
#     print (i)
#     aa.add(tuple(i))
# print (aa)