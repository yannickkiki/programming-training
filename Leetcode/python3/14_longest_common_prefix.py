class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        left, right = 0, len(strs[0])
        while left<right:
            val = (left+right)//2
            model = strs[0][:1+val]
            is_broken = False
            for string in strs[1:]:
                if string[:1+val] != model:
                    is_broken = True
                    break
            if is_broken:
                right = val
            else:
                left = val+1
        return strs[0][:left]


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert s.longestCommonPrefix(["flowere","fo","flowere"]) == "f"
    assert s.longestCommonPrefix(["fl","fl","fl"]) == "fl"
    