#not working
class Solution:
    def trap(self, height):
        result = 0
        i = 0
        n = len(height)
        while height[i] < height[i+1]:
            i += 1
        j = i
        while j < n-1:
            if (height[j] > height[j+1] and height[j] >= height[i]):
                i = j
            else:
                result += max(0, height[i]-height[j])
            j += 1
        return result
    

if __name__ == '__main__':
    s = Solution()
    result = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    # assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
