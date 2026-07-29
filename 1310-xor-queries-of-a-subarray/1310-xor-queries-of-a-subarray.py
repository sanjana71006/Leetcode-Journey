class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        n=len(arr)
        prefix=[0]*n
        prefix[0]=arr[0]
        for i in range(1,n):
            prefix[i]=arr[i]^prefix[i-1]
        for l,r in queries:
            if l==0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r]^prefix[l-1])
        return ans
            
