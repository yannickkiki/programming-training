class Solution:
    def exploreWings(self, left, right):
        while(left>=0 and right<self.n and self.s[left]==self.s[right]):
            left -= 1
            right += 1
        return right-left-1
    
    def longestPalindrome(self, s):
        if not s:
            return ""
        self.s = s
        self.n = len(s)
        result = ""
        for i in range(self.n):
            l1 = self.exploreWings(i, i)
            l2 = self.exploreWings(i, i+1)
            if l1>l2:
                if l1>len(result):
                    result = self.s[i-l1//2: i+l1//2+1]
            else:
                if l2>len(result):
                    result = self.s[i-(l2-2)//2:i+(l2-2)//2+2]
        return result

if __name__ == '__main__':
    s = Solution()
    result = s.longestPalindrome("aaxxab")
