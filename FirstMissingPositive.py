__author__ = 'Jie'
"""
41. First Missing Positive
Hard
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution:
    def firstMissingPositive(self, nums) -> int:
        n=len(nums)
        # use the hash idea
        #after observation, the idea is the ith element should be in the ith-0 slot.

        for i in range(n):
            # num[i]-1 is the index of the element which is supoosed to be location, nums[i] is the ith element.
            while nums[i]>0 and nums[i]<=n and nums[nums[i]-1] !=nums[i]:
                # print (i)
                self.swap(nums,nums[i]-1,i)
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        # if  nums is empty
        return n+1

    def swap(self,nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]

solution=Solution()
# nums=[3,4,-1,1]
nums=[0,1,2]
ans=solution.firstMissingPositive(nums)
print (ans)