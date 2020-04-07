__author__ = 'Jie'
"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # naive method
        if nums1 is None and nums2 and len(nums2)%2==1:
            return nums2[len(nums2)//2]
        if nums1 is None and nums2 and len(nums2)%2==0:
            return (nums2[len(nums2)//2]+nums2[len(nums2)//2-1])/2
        if nums2 is None and nums1 and len(nums1)%2==1:
            return nums1[len(nums1)//2]
        if nums2 is None and nums1 and len(nums1)%2==0:
            return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2

        if nums1 and nums2:
            nums1.extend(nums2)
            nums1.sort()
            leng=len(nums1)
            if leng%2==1:
                return nums1[leng//2]
            else:
                return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
solution=Solution()
nums1 = [ ]
nums2 = [1,3]
ans=solution.findMedianSortedArrays(nums1,nums2)
print (ans)

# nums1 = [1, 3]
# nums2 = [2,2,2]
# nums1.extend(nums2)
# nums1.sort()
#
# print (nums1)
