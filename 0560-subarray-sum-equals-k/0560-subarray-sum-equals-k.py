class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0: 1}   
        prefSum = 0
        res = 0
        for i in nums:
            prefSum += i
            res += dct.get(prefSum - k, 0)
            dct[prefSum] = dct.get(prefSum, 0) + 1

        return res