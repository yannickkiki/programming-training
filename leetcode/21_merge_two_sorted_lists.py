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
    def mergeTwoLists(self, l1, l2):
        root = node = ListNode(None)
        while True:
            if not l1:
                node.next = l2
            elif not l2:
                node.next = l1
            if not l1 or not l2:
                break

            min_val = None
            if l1.val < l2.val:
                min_val = l1.val
                l1 = l1.next
            else:
                min_val = l2.val
                l2 = l2.next
            new_node = ListNode(min_val)
            node.next = new_node
            node = new_node
        return root.next
    


if __name__ == '__main__':
    s = Solution()
    result = s.mergeTwoLists(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]))