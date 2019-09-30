from copy import deepcopy

class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def build_linked_list(l):
    node = ListNode(l[0])
    for idx in range(1, len(l)):
        old_node = deepcopy(node)
        node = ListNode(l[idx])
        node.next = old_node
    return node
        

def get_next(l):
    return l.next if l else None

def get_val(l):
    return l.val if l else 0

def retain_and_rest(v1, v2, old_retain=0):
    v = v1 + v2 + old_retain
    return v//10, v%10
    
def addTwoNumbers(l1, l2):
    retain, l_val = retain_and_rest(l1.val, l2.val)
    l = ListNode(l_val)
    old_node = l
    while True:
        l1, l2 = get_next(l1), get_next(l2)
        if l1 or l2:
            l1_val, l2_val = get_val(l1), get_val(l2)
            retain, l_val = retain_and_rest(l1_val, l2_val, retain)
            node = ListNode(l_val)
            old_node.next = node
            old_node = node
        else:
            if retain:
                node = ListNode(retain)
                old_node.next = node
                old_node = node
            break
    return l
        

l1 = build_linked_list([3, 4, 2])
l2 = build_linked_list([4, 6, 5])
l = addTwoNumbers(l1, l2)