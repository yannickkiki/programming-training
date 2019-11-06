class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

       
def build_tree(arr):
    idx, n, nodes = 0, len(arr), [TreeNode(x) for x in arr]
    while True:
        left_idx, right_idx = 2*idx + 1, 2*idx + 2

        if left_idx < n:
            nodes[idx].left = nodes[left_idx]
        else:
            break

        if right_idx < n:
            nodes[idx].right = nodes[right_idx]
        else:
            break
        
        idx+=1

    return nodes[0]


class Solution:
    def rangeSumBST(self, root, L, R):
        self.sum_ = 0
        def make_sum(node):
            if node and node.val:
                if L <= node.val <= R:
                    self.sum_ += node.val
                if node.val < R:
                    make_sum(node.right)
                if node.val > L:
                    make_sum(node.left)
        
        make_sum(root)
            

s = Solution()

root = build_tree([10, 5, 15, 3, 7, None, 18])
s.rangeSumBST(root, 7, 15)
assert s.sum_ == 32

root = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
s.rangeSumBST(root, 6, 10)
assert s.sum_ == 23
