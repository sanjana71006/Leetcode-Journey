import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        heap=[-num for num in nums]
        heapq.heapify(heap)
        n=len(nums)
        if n>=3:
            for _ in range(2):
                heapq.heappop(heap)
            return -heapq.heappop(heap)
        else:
            return -heapq.heappop(heap)
