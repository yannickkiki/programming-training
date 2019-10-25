from queue import PriorityQueue

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
        q = PriorityQueue()
        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, idx))
        while not q.empty():
            min_val, min_idx = q.get()
            new_node = ListNode(min_val)
            node.next = new_node
            node = new_node
            lists[min_idx] = lists[min_idx].next
            if lists[min_idx]:
                q.put((lists[min_idx].val, min_idx))
        return root.next


if __name__ == '__main__':
    s = Solution()
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]
    result = s.mergeKLists(lists)
