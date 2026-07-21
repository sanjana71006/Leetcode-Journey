class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,h=1,x//2
        while l<=h:
            mid=(l+h)//2
            sq=mid*mid
            if sq==x:
                return mid 
            elif sq<x:
                l=mid+1
            else:
                h=mid-1
        return h

