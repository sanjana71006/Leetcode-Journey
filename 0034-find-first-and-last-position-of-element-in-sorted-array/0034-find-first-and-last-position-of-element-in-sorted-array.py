class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,h=0,len(nums)-1
        mini=maxi=-1
        while l<=h:
            m=(l+h)//2 
            if nums[m]==target:
                mini=m
                h=m-1
            elif nums[m]>target:
                h=m-1 
            else:
                l=m+1 
        l,h=0,len(nums)-1
        while l<=h:
            m=(l+h)//2 
            if nums[m]==target:
                maxi=m
                l=m+1
            elif nums[m]>target:
                h=m-1 
            else:
                l=m+1 
        return mini,maxi