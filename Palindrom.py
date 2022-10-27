class Solution:
    def isPalindrome(self,x):
        y=str(x)
        sum=0
        indx=-1
        for i in range(len(y)):
            islem=divmod(x,10)
            sum+=islem[1]*(10**(len(y)+indx))
            indx+=-1
            x=islem[0]
            print( islem[0],islem[1],sum)
        if sum==int(y):
            return True
        else:
            return False
a=Solution()
print(a.isPalindrome(121))





