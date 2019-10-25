MAX = float('inf')


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


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return

        root = node = ListNode(None)
        while True:
            min_, min_idx, comp = MAX, None, 0
            for idx, l in enumerate(lists):
                if not l:
                    comp += 1
                    continue
                if l.val < min_:
                    min_idx = idx
                    min_ = l.val
            if comp == len(lists):
                break
            new_node = ListNode(min_)
            node.next = new_node
            node = new_node
            lists[min_idx] = lists[min_idx].next
        return root.next


if __name__ == '__main__':
    s = Solution()
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]
    result = s.mergeKLists(lists)
