class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def generate_LN(l):
    head = ListNode(l[0])
    p = head
    if len(l) == 1:
        return head

    for i in l[1:]:
        p.next = ListNode(i)
        p = p.next
    return head

def print_LN(head):
    l = []
    p = head
    while(p):
        l.append(p.val)
        p = p.next
    print(l)
    return l


l1 = generate_LN([1,3,5])
l2 = generate_LN([1,2,4,8])
print_LN(l1)
print_LN(l2)

def merge(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    head = ListNode(0)
    p1,p2,p = l1,l2,head

    while p1 and p2:
        if p1.val <= p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next

        p = p.next
    p.next = p1 or p2
    return head.next


def merge2(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = merge2(l1.next, l2)
        return l1
    else:
        l2.next = merge2(l1,l2.next)
        return l2






l3 = merge2(l1,l2)
print_LN(l3)