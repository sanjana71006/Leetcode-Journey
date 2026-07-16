class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        ps=nums.copy()
        for i in range(1,n):
            ps[i]=ps[i]+ps[i-1]
        ss=nums.copy()
        for i in range(n-2,-1,-1):
            ss[i]=ss[i]+ss[i+1]
        for i in range(0,n):
            if ss[i]==ps[i]:
                return i 
        return -1
        