from . import utils

class Solution:
    def removeNthFromEnd(self, head, n):
        root = utils.ListNode(None)
        first = root.next = head
        second = root
        
        for i in range(n):
            first = first.next
        if not first:
            return head.next
        
        while first:
            second = second.next
            first = first.next
        
        second.next = second.next.next
        
        return head
        

if __name__ == '__main__':
    s = Solution()
    result = s.removeNthFromEnd(utils.build_linked_list([1, 2, 3, 4]), 2)
