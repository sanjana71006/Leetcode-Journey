class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1
        l,h=0,len(nums)-1
        while l<=h:
            i=(l+h)//2
            mid=nums[i]
            if mid==target:
                return i
            elif mid<target:
                l=i+1
            else:
                h=i-1
        return -1

