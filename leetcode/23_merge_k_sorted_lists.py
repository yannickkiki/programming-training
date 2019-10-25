from copy import deepcopy

MAX = float('inf')


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(l):
    if not l:
        return
    n = len(l)
    node = ListNode(l[n-1])
    for idx in range(n-2, -1, -1):
        old_node = deepcopy(node)
        node = ListNode(l[idx])
        node.next = old_node
    return node


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return

        result = list()
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
            result.append(lists[min_idx].val)
            lists[min_idx] = lists[min_idx].next
        return build_linked_list(result)


if __name__ == '__main__':
    s = Solution()
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]
#    lists = [build_linked_list([]), build_linked_list([1, 4, 5])]
    result = s.mergeKLists(lists)
