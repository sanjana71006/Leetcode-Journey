from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        while low<high:
            mid=(low+high)//2
            hrs=0
            for pile in piles:
                hrs+=(pile+mid-1)//mid 
            if hrs<=h:
                high=mid
            else:
                low=mid+1
        return low
        