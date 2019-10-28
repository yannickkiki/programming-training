def is_subfolder(subfolder, folder):
    return subfolder[:1+len(folder)] == folder+"/"


class Solution:
    def removeSubfolders(self, folders):
        folders.sort()
        n, result, supfolder_idx, i = len(folders), folders[:1], 0, 1
        # print(folders, result)
        while i < n:
            # print(i)
            if not is_subfolder(folders[i], folders[supfolder_idx]):
                result.append(folders[i])
                supfolder_idx = i
            i += 1
        return result

 
if __name__ == '__main__':
    s = Solution()
    assert sorted(s.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])) == sorted(["/a", "/c/d", "/c/f"])
    assert s.removeSubfolders(["/a","/a/b/c","/a/b/d"]) == ["/a"]
    assert sorted(s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])) == sorted(["/a/b/c","/a/b/ca","/a/b/d"])
