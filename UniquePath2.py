__author__ = 'Jie'
"""
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        # use DP as well, set the obstacle cell to 0, since there is no way to path at such cell
        m=len(obstacleGrid)  # the number of rows
        n=len(obstacleGrid[0])  # the number of columns

        ## if the obstacle is at the beginning, there is no way to path. return 0
        if obstacleGrid[0][0]==1: return 0
        ## set the inital value in the first column and the first row
        # if there is an obstacle, set this cell to 0; otherwise,the one is equal to the previous one: ob[0][j]=ob[0][j-1]+ob[0-1][j]
        # ob[0-1][j] does not exsit, since it is out of boundary
        obstacleGrid[0][0]=1
        for i in range(1,n):
            if obstacleGrid[0][i]==1:
                obstacleGrid[0][i]=0
            else:
                obstacleGrid[0][i]=obstacleGrid[0][i-1]

        for i in range(1,m):
            if obstacleGrid[i][0]==1:
                obstacleGrid[i][0]=0
            else:
                obstacleGrid[i][0]=obstacleGrid[i-1][0]
        # using dp
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return obstacleGrid[m-1][n-1]

soltuion=Solution()
obstacleGrid=[[0,0],[1,1],[0,0]]
ans=soltuion.uniquePathsWithObstacles(obstacleGrid)
print (ans)
