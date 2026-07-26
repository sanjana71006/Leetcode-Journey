class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        prefixsum=nums[0] 
        for i in range(1,len(nums)):
            prefixsum=max(prefixsum+nums[i],nums[i]) 
            ans=max(ans,prefixsum) 
        return ans
