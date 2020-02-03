class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    assert s.strStr("hello", "ll") == 2
    assert s.strStr("aaaaa", "bba") == -1
    assert s.strStr("hello", "") == 0
    assert s.strStr("", "") == 0
