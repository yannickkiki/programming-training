import xlib


class Solution:
    def partition(self, head: xlib.ListNode, x: int) -> xlib.ListNode:
        pass


if __name__ == '__main__':
    s = Solution()

    head = xlib.build_linked_list([1, 4, 3, 2, 5, 2])
    partition = s.partition(head, x=3)

    result = xlib.get_list_from_linked_list(head)

    assert result == [1, 2, 2, 4, 3, 5]
