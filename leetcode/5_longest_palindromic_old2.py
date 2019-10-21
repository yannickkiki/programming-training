class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        is_palindrome, n = dict(), len(s)

        # handle string size = 1
        for j in range(n):
            is_palindrome[(j, j+1)] = True

        result = s[0]

        # handle string size = 2
        for j in range(n-1):
            is_palindrome[(j, j+2)] = s[j] == s[j+1]
            if is_palindrome[(j, j+2)]:
                result = s[j:j+2]

        # handle string size >= 3
        for i in range(3, n+1):
            for j in range(n-i+1):
                is_palindrome[(j, j+i)] = s[j] == s[j+i-1] and is_palindrome[(j+1, j+i-1)]
                if is_palindrome[(j, j+i)]:
                    result = s[j:j+i]

        return result

if __name__ == '__main__':
    s = Solution()
    result = s.longestPalindrome("abacab")