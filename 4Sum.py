__author__ = 'Jie'
"""
18. 4Sum

Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution:
    def fourSum(self, nums, target: int):
        n=len(nums)
        nums.sort()
        result=[]

        for i in range(n-3):
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[-1]+nums[-2]+nums[-3]<target:
                continue
            if i>0 and nums[i]==nums[i-1]:
                # if the first index is duplicated, continue, jump to the next element.
                continue

            for j in range(i+1,n-1):
                # if the second index is duplicated, jump to the new element.
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                m=j+1
                r=n-1
                while m<r:
                    tmp=nums[i]+nums[j]+nums[m]+nums[r]
                    if tmp==target:
                        result.append([nums[i],nums[j],nums[m],nums[r]])
                        while m+1<r and nums[m]==nums[m+1]:
                            m+=1
                        while r-1> m  and nums[r]==nums[r-1]:
                            r-=1
                        m+=1
                        r-=1
                    elif tmp<target:
                        m+=1
                    else:
                        r-=1
        return result



if __name__ == '__main__':
    solution=Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target=0
    ans=solution.fourSum(nums,target)
    print (ans)



