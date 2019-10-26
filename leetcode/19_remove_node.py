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
    def removeNthFromEnd(self, head, n):
        root = ListNode(None)
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
    result = s.removeNthFromEnd(build_linked_list([1, 2, 3, 4]), 2)
