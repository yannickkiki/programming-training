class Solution:
    def canJump(self, nums):
        idx, last_reachable_idx, n = 0, 0, len(nums)
        while idx <= last_reachable_idx:
            last_reachable_idx = max(idx+nums[idx], last_reachable_idx)
            if last_reachable_idx >= n-1:
                return True
            idx += 1
        return False


if __name__ == '__main__':
    s = Solution()
    assert s.canJump([2,3,1,1,4]) == True
    assert s.canJump([3,2,1,0,4]) == False
