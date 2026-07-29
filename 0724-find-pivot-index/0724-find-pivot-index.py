class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps=nums.copy()
        n=len(nums)
        for i in range(1,n):
            ps[i]=ps[i-1]+ps[i]
        ss=[0]*n
        ss[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            ss[i]=nums[i]+ss[i+1]
        for i in range(n):
            if ss[i]==ps[i]:
                return i
        return -1
