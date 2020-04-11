__author__ = 'Jie'
# -*- coding: utf-8 -*-
"""
31. Next Permutation
this is one is tough !!!
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
"""
class Solution:
    def swap(self,nums,indexi,indexj):
        # this is a help function for swap element
        nums[indexi],nums[indexj]=nums[indexj],nums[indexi]

    def reverse(self,nums,start, end):
        # this is a help function for reverse element from the start location to the end location
        while start<end:
            self.swap(nums,start,end)
            start+=1
            end -=1
        return nums

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n==1:
            return nums
        if n==2:
            self.swap(nums,0,1)
            return nums
        dec=n-2 # the last element in nums has nothing to reverse.
        while dec>=0 and nums[dec]>=nums[dec+1]:
            # searching the index that would start to reverse. the first elemetn in decending order from the back.
            dec-=1
        self.reverse(nums,dec+1,n-1)
        # print (nums)
        # print (dec)
        if dec==-1:
            # this is the case the arrangement is not possible, it should return the lowest posssible order
            return nums
        next_num=dec+1
        while next_num<n and nums[next_num]<=nums[dec]:
            #keep searching the index so that find the maximum element in nums is found, and then swap
            next_num+=1
        self.swap(nums,next_num,dec)
        return nums

nums=[1,2,7,9,6,4,1]
# nums=[3,2,1]
solution=Solution()
ans=solution.nextPermutation(nums)
print (ans)

# ans1=solution.reverse(nums,0,6)
# print (ans1)
