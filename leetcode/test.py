class Solution:
    def maxArea(self, heights):
        maxarea = 0
        l = 0
        r = len(heights) - 1;
        while l < r:
            maxarea = max(maxarea, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea

if __name__ == '__main__':
    s = Solution()
    result = s.maxArea([7, 8, 5, 6])
