class Solution:
    def trap(self, height):
        n = len(height)
        left_max, right_max = height[:1]+[0]*(n-1), [0]*(n-1)+height[-1:]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            right_max[n-i-1] = max(right_max[n-i], height[n-i-1])
        result = 0
        for i in range(n):
            result += min(left_max[i], right_max[i])-height[i]
        return result
            

if __name__ == '__main__':
    s = Solution()
    result = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    # assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6