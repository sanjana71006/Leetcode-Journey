class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0]*n
        for i in range(n):
            nums[i]=start+2*i 
        ans=0
        for num in nums:
            ans^=num
        return ans