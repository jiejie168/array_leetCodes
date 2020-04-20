__author__ = 'Jie'
# -*- coding: utf-8 -*-
"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid) -> int:
        ## DP. grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
        m=len(grid)
        n=len(grid[0])

        if m==1 and n==1: return grid[0][0]
        ## initial the values for Dp
        grid[0][0]=grid[0][0]
        for i in range(1,m):
            grid[i][0]=grid[i][0]+grid[i-1][0]
        for i in range(1,n):
            grid[0][i]=grid[0][i]+grid[0][i-1]

        # start to use the DP
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]

    def minPathSum_1(self,grid):
        # recursive method, with extra memory.
        # this method is current not succeful
        m=len(grid)
        n=len(grid[0])
        result=[]
        for i in range(m):
            result.append([0 for j in range(n)])

        def help_recurs(grid,x,y,m,n):
            # recursive function
            if x==0 and y==0: return grid[x][y]
            # if x<0 or y<0: return float('inf')
            if result[x][y]>0: return result[x][y]
            ans=grid[x][y]+min(help_recurs(grid,x-1,y,m,n),help_recurs(grid,x,y-1,m,n))
            result[x][y]=ans
        return help_recurs(grid,m-1,n-1,m,n)

solution=Solution()
grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
# ans=solution.minPathSum(grid)
ans=solution.minPathSum_1(grid)
print (ans)


