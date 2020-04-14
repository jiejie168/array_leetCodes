__author__ = 'Jie'
"""
42. Trapping Rain Water
Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height) -> int:
        # naive algorithm
        # search the left max height of an element the right max height of an element,
        #find the maximum level of water it can trap after the rain,
        # which is equal to the minimum of maximum height of bars on both the sides minus its own height.
        n=len(height)
        result=0
        for i in range(1,n):
            ##
            lmax=height[i] # this is important, can not be set to 0
            rmax=height[i]
            for j in range(i):
                lmax=max(lmax,height[j])
            for k in range(i+1,n):
                rmax=max(rmax,height[k])
            result+=min(lmax,rmax)-height[i]
        return result

    def trap_dp(self,height):
        # dynamic programming;  cannot pass in leetcode. runtime error.
        #pre-compute the highest bar on both sides of each element, then use this for further calculation of water volumns
        n=len(height)
        left=n*[0]
        right=n*[0]
        water=0
        # fill the left bar
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        right[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        for i in range(n):
            water+=min(left[i],right[i])-height[i]

        return water

height=[0,1,0,2,1,0,1,3,2,1,2,1]
solution=Solution()
# ans=solution.trap(height)
ans=solution.trap_dp(height)
print (ans)


