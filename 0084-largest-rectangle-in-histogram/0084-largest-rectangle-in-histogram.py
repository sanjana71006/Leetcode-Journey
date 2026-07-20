from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                ans = max(ans, h * w)

            stack.append(i)

        return ans