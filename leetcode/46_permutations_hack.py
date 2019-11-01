from itertools import permutations


class Solution:
    def permute(self, nums):
        return [list(p) for p in permutations(nums)]
    

if __name__ == '__main__':
    s = Solution()
    assert sorted(s.permute([1, 2, 3])) == sorted([[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]])
        