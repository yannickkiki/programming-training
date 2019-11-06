class Solution:
    def maxArea(self, heights):
        n = len(heights)
        left_idx, right_idx, s = 0, n-1, 0
        while left_idx < right_idx:
            left_h, right_h = heights[left_idx], heights[right_idx]
            s = max(s, (right_idx-left_idx)*min(left_h, right_h))
            if left_h<right_h:
                left_idx += 1
            else:
                right_idx -= 1
        return s
            
if __name__ == '__main__':
    s = Solution()
    result1 = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) # 49
    result2 = s.maxArea([2, 3, 4, 5, 18, 17, 6]) # 17
