__author__ = 'Jie'
"""
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n: int):
        # no special algorithm, just use many loops
        matrix=[]
        # construct an empty n*n matrix
        for i in range(n):
            matrix.append([0 for j in range(n)])
        col_s=0
        col_e=n-1
        row_s=0
        row_e=n-1
        number=1

        while col_s<=col_e and row_s<=row_e:
            for i in range(col_s,col_e+1):
                # first loop for the first row
                matrix[row_s][i]=number
                number+=1
            row_s+=1
            for i in range(row_s,row_e+1):
                # second loop for the last column
                matrix[i][col_e]=number
                number+=1
            col_e-=1

            # if row_s<=row_e:
            # to avoid the overflow of small cases
            for i in range(col_e,col_s-1,-1):
                # third loop for the last row
                matrix[row_e][i]=number
                number+=1
            row_e-=1

            # if col_s<=col_e:
            for i in range(row_e,row_s-1,-1):
                # forth loop for the fist column
                matrix[i][col_s]=number
                number+=1
            col_s+=1
        return matrix

solution=Solution()
ans=solution.generateMatrix(2)
print (ans)


