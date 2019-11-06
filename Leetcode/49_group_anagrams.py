from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for s in strs:
            result["".join(sorted(s))].append(s)
        return list(result.values())


if __name__ == '__main__':
    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
