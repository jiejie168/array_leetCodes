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
        # use the binary search method for the much shorter array
        m=len(nums1)
        n=len(nums2)
        ##  make sure that the nums1 is alway the short array for search in order to save searching time.
        if m>n:
            nums1,nums2,m,n=nums2,nums1,n,m

        ## initiate the original index for binary search
        imin,imax=0,m
        while imin<=imax:
            # binary search; cutA is the partition index of left part of nums1, cutB is the
            # is the partition index of the left part of nums2
            cutA=(imin+imax)//2
            cutB=(m+n+1)//2-cutA
            # compare the left part maximum value of nums2 and the right part minimum value of nums1,
            # is so, search to the left for nums2, then increase imin.
            # if cutA=m, it means that the right part of nums1[] is empty.
            if cutA < m and nums1[cutA]<nums2[cutB-1]:
                imin=cutA+1
            ## if cutA=0, it means that the left part of nums1[] is empty.
            ## search to the right for nums2.
            elif cutA>0  and nums1[cutA-1]>nums2[cutB]:
                imax=cutA-1
            # the search criteria reaches.
            else:
                # situation 1: the left part of nums1[] is empty, so median is selected as the maximum value of the left
                # part of nums2[]
                if cutA==0:
                    median=nums2[cutB-1]
                #situation 2.similar with the former part
                elif cutB==0:
                    median=nums1[cutA-1]
                ## situation 3, selct the maximum value of the left group.
                else:
                    median=max(nums1[cutA-1],nums2[cutB-1])
                break
        # get out the loop after partition.
        # if the overall length is odd, return only one element
        if (m+n) %2==1:
            return median
        # situation 2 for an even length
        if cutA==m:
            return (median+nums2[cutB])/2
        # situation 3 for an even length
        if cutB==n:
            return (median+nums1[cutA])/2
        # situation 4 for an even length
        min_of_right=min(nums1[cutA],nums2[cutB])
        return (median+min_of_right)/2

# solution=Solution()
nums1=[5,6]
nums2=[1,2,3,4,7]
# ans=solution.findMedianSortedArrays(nums1,nums2)

