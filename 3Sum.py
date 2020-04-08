__author__ = 'Jie'
"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        n=len(nums)
        nums.sort()
        result=[]
        for i in range (n-2):
            #  first list several exceptions
            # the first three elements sum is larger than 0, which means there is no solution
            # the first and the last two elements is less than 0, which means the first element is too small, get out of this element
            # if two consecutive elements, jump.
            if nums[i]+nums[i+1]+nums[i+3]>0:
                break
            if nums[i]+nums[-1]+nums[-2]<0:
                continue
            if i>0 and nums[i]==nums[i-1]:
                continue

            l,r=i+1,n-1  #  two pointers, search from both ends.
            while l<r:
                tmp=nums[i]+nums[l]+nums[r]
                if tmp==0:
                # match the result
                    result.append([nums[i],nums[l],nums[r]])
                    #### we have to search for the duplicate scenarios. only two elements are allowed to be duplicated.
                    # skip duplicate element nums[l+1]
                    while l+1<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r-1 and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif tmp<0:
                    # it means that the value should increase.The search goes to the right
                    l+=1
                else:
                    # it means that the value should decrease. The search goes to the left
                    r-=1
        return result

solution=Solution()
nums=[-1, 0, 1, 2, -1, -4]
ans=solution.threeSum(nums)
print (ans)








