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

        idx += 1

    return nodes[0]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(l):
    if not l:
        return
    n = len(l)
    root = node = ListNode(None)
    for idx in range(0, n):
        new_node = ListNode(l[idx])
        node.next = new_node
        node = new_node
    return root.next


def get_list_from_linked_list(head):
    result = list()
    while head:
        result.append(head.val)
        head = head.next
    return result
