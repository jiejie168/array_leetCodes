__author__ = 'Jie'
"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution:
    def maxArea(self, height) -> int:
        # method 1, naive method
        max_area=0
        for i in range(len(height)):
            for j in range(1,len(height)):
                area=abs(j-i)*min(height[i],height[j])
                max_area=max(max_area,area)
        return max_area

    def maxArea_2(self,height):
        # two pointers
        max_area=0
        i=0  # the left pointer
        j=len(height)-1  # the right pointer
        while i<j:
            area=abs(j-i)*min(height[i],height[j])
            max_area=max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area

solution=Solution()
height=[1,8,6,2,5,4,8,3,7]
# ans=solution.maxArea(height)
ans=solution.maxArea_2(height)
print (ans)
