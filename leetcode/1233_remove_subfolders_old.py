#time limit exceeded


def is_subfolder(subfolder, folder):
    return subfolder[:1+len(folder)] == folder+"/"


class Solution:
    def removeSubfolders(self, folders):
        folders.sort(key=lambda item: len(item))
        n = len(folders)
        is_removed = [False]*n
        for i in range(n):
            for j in range(i+1, n):
                # print(folders[j], folders[i])
                if is_subfolder(folders[j], folders[i]):
                    is_removed[j] = True
        # print(is_removed)
        return [folder for i, folder in enumerate(folders) if not is_removed[i]]


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])) == sorted(["/a", "/c/d", "/c/f"])
    assert s.removeSubfolders(["/a","/a/b/c","/a/b/d"]) == ["/a"]
    assert sorted(s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])) == sorted(["/a/b/c","/a/b/ca","/a/b/d"])
