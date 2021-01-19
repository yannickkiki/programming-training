# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_decimal_value(self, head: ListNode) -> int:
        result = head.val
        head = head.next
        while head:
            result = result * 2 + head.val
            head = head.next
        return result


if __name__ == '__main__':
    import xlib

    s = Solution()

    assert s.get_decimal_value(xlib.build_linked_list([1, 0, 1])) == 5
    assert s.get_decimal_value(xlib.build_linked_list([0])) == 0
    assert s.get_decimal_value(xlib.build_linked_list([1])) == 1
    assert s.get_decimal_value(xlib.build_linked_list([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880
    assert s.get_decimal_value(xlib.build_linked_list([0, 0])) == 0
    print("Success!")
