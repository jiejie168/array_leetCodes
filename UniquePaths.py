__author__ = 'Jie'
"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.path_recurs(m,n)

    def path_recurs(self,m,n):
        ## recursive method
        # first construct the termination condition of recursion
        if m<0 or n<0: return 0
        if m==1 and n==1: return 1
        return self.path_recurs(m-1,n)+self.path_recurs(m,n-1)

    def uniquePaths_dp(self,m,n):
        #  provided the array for data restore
        if m<0 or n<0: return 0
        result=[]
        for i in range(m):
            result.append([None for j in range(n)])

        # set the initial values in the first column and the first row !
        for i in range(n):
            result[0][i]=1
        for i in range(m):
            result[i][0]=1

        for i in range(1,m):
            # m is the row number, n is the column number
            # use the Dp technique
            for j in range(1,n):
                result[i][j]=result[i-1][j]+result[i][j-1]
        return result[m-1][n-1]

m=7
n=3
solution=Solution()
# ans=solution.uniquePaths(m,n)
ans=solution.uniquePaths_dp(m,n)
print (ans)