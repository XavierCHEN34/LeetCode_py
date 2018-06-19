
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


head1 = generate_LN([1,3,5,7,9])
print_LN(head1)




def removeNthFromEnd(head, n):
    p = head
    l = []
    while(p):
        l.append(p.val)
        p = p.next
    del l[-n]
    p = generate_LN(l)
    return p

new = removeNthFromEnd(head1,2)
print_LN(new )
