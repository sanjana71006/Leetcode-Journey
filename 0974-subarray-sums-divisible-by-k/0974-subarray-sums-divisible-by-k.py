class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp={0:1}
        n=len(nums)
        ans=0
        prefix=0
        for num in nums:
            prefix+=num 
            rem=prefix%k
            if rem in mp:
                ans+=mp[rem]
            mp[rem]=mp.get(rem,0)+1 
        return ans
        

