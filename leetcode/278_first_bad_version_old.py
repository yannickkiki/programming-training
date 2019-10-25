IS_BAD_VERSION = {1: False, 2: False, 3: True, 4: True, 5: True, 6: True}


def isBadVersion(version):
    return IS_BAD_VERSION[version]


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        diff_1_comp = 0
        while True:
            v = (left+right)//2

            if v == left:
                if diff_1_comp == 1:
                    v = right
                if diff_1_comp == 2:
                    break
                diff_1_comp += 1

            if isBadVersion(v):
                if not isBadVersion(v-1):
                    return v
                right = v
            else:
                left = v


if __name__ == '__main__':
    s = Solution()
    result = s.firstBadVersion(5)
