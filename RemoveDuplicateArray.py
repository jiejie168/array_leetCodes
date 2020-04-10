__author__ = 'Jie'
"""

"""
class Solution:
    def removeElement(self, nums, val: int) -> int:
        if nums is None:
            return 0

        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        # count=len(nums)
        return nums

nums=[0,1,2,2,3,0,4,2]
val=2
solution=Solution()
ans=solution.removeElement(nums,val)
print (ans)
