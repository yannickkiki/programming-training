class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort()
        result = list()
        current_interval = intervals[0]
        for interval in intervals[1:]:
            if current_interval[1] >= interval[0]:
                current_interval = [min(current_interval[0], interval[0]), max(current_interval[1], interval[1])]
            else:
                result.append(current_interval)
                current_interval = interval[:]
        result.append(current_interval)
        return result
            

if __name__=='__main__':
    s = Solution()
    assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
