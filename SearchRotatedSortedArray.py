__author__ = 'Jie'
"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""

class Solution:
    def search(self, nums, target: int) -> int:
        # hash_table method,  runtime complexity : O(n)
        if target not in nums:
            return -1
        n=len(nums)
        from collections import defaultdict
        hash_table=defaultdict(int)
        for i in range(n):
            hash_table[nums[i]]=i
        if target in hash_table:
            return hash_table[target]

    def serach_1(self,nums,target):
        # binary search, runtime complexity is O(log(n))
        left,right=0,len(nums)-1
        while left <=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if target>=nums[0]:
                ## judge if target is in left or in right parts.
                ## the target is in the left ascending part
                if nums[mid]>=nums[0] and nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            else:
                # the target is in the right part
                if nums[mid]>=nums[0] or nums[mid] <target:
                    left=mid+1
                else:
                    right=mid-1
        return -1

nums=[4,5,6,7,0,1,2]
target=7
solution=Solution()
ans=solution.serach_1(nums,target)
print (ans)