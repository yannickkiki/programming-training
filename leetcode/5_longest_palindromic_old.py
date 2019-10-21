class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        is_palindrome, n, result = {"": True}, len(s), ""

        for i in range(1, n+1):
            for j in range(n-i+1):
                substring = s[j:j+i]
                is_palindrome[substring] = substring[0]==substring[-1] and is_palindrome[substring[1:-1]]
                if is_palindrome[substring]:
                    result = substring

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.longestPalindrome("abacab")
