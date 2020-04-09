__author__ = 'Jie'
"""
16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example:

Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        n=len(nums)
        nums.sort()
        result=nums[0]+nums[1]+nums[-1]

        for i in range(n-2):
            # first skip the duplicated element, since it would be the same with the former loop
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                tmp=nums[i]+nums[l]+nums[r]
                # always put the minimun sum into result for final output
                if abs(tmp-target)<abs(result-target):
                    result=tmp
                # update l,r depending on comparison
                if tmp==target:
                    return target
                elif tmp<target:
                    l+=1
                else:
                    r-=1
        return result

solution=Solution()
nums = [-1, 2, 1, -4]
target = 1
ans=solution.threeSumClosest(nums,target)
print (ans)
