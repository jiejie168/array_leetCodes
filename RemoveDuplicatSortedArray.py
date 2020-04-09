__author__ = 'Jie'
"""
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        # two pointers
        count=0
        n=len(nums)
        if n==0:
            return 0

        for i in range(n):
            if nums[count]!=nums[i]:
                count+=1
                nums[count]=nums[i]

        return count+1,nums
nums=[1,1,2]
solution=Solution()
ans,ans1=solution.removeDuplicates(nums)
print(ans)
print (ans1)