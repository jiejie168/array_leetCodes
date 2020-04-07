__author__ = 'Jie'
"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target: int):
        # naive method
        for i in range(len(nums)):
            sub=target-nums[i]
            for j in range(i+1,len(nums)):
                if sub==nums[j]:
                    return [i,j]
    def twoSum_1(self,nums,target):
        # an effective method, hash_table
        new_hash={}
        for i,elem in enumerate(nums):
            sub=target-elem
            if sub not in new_hash:
                new_hash[elem]=i
            else:
                return [new_hash[sub],i]

solution=Solution()
sums=[2, 7, 11, 15]
target=9
# array_1=solution.twoSum(sums,target)
array_1=solution.twoSum_1(sums,target)
print (array_1)


