import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        heap=[]
        ans=[]
        for i,j in freq.items():
            heapq.heappush(heap,(-j,i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
