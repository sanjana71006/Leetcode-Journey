class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        left = 0
        curr_sum = 0
        ans = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            mp[nums[right]] = mp.get(nums[right], 0) + 1

            if right - left + 1 > k:
                curr_sum -= nums[left]
                mp[nums[left]] -= 1
                if mp[nums[left]] == 0:
                    del mp[nums[left]]
                left += 1

            if right - left + 1 == k and len(mp) == k:
                ans = max(ans, curr_sum)

        return ans