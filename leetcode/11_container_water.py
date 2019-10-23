class Solution:
    def maxArea(self, heights):
        n = len(heights)
        left_idx, right_idx, cursor = 0, n-1, 1
        left_h, right_h = heights[left_idx], heights[right_idx]
        h = min(left_h, right_h)
        s = (right_idx-left_idx)*h
        print("(0)", left_idx, right_idx, h, s)

        while cursor < right_idx:
            print("Cursor idx", cursor)
            current_h = heights[cursor]
            if current_h >= h:
                left_s = (cursor-left_idx)*min(left_h, current_h)
                right_s = (right_idx-cursor)*min(current_h, right_h)

                if left_s > s and left_s > right_s:
                    right_idx = cursor
                    right_h = heights[cursor]
                    h = min(left_h, right_h)
                    s = (right_idx-left_idx)*h
                    print("(1)", left_idx, right_idx, h, s)
                elif right_s > s and right_s > left_s:
                    left_idx = cursor
                    left_h = heights[cursor]
                    h = min(left_h, right_h)
                    s = (right_idx-left_idx)*h
                    print("(2)", left_idx, right_idx, h, s)
            cursor += 1
        
        return s


if __name__ == '__main__':
    s = Solution()
    # result = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) #49
    result = s.maxArea([2, 3, 4, 5, 18, 17, 6])
