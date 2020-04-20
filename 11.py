__author__ = 'Jie'

class Solution:
    def plusOne(self, digits):
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        digits[0]=1
        digits.append(0)
        return digits
solution=Solution()
array=[1,2,9,9]
digit=solution.plusOne(array)
print (digit)