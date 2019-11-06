IS_BAD_VERSION = {1: False, 2: False, 3: False, 4: True, 5: True, 6: True}


def isBadVersion(version):
    return IS_BAD_VERSION[version]


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            v = (left+right)//2
            if isBadVersion(v):
                right = v
            else:
                left = v+1
        return left


if __name__ == '__main__':
    s = Solution()
    result = s.firstBadVersion(5)
