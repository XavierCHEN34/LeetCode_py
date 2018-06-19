
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






"""
creat a val_list, reverse the val_list then modify the value of LN
"""

def reverse_linked_list1(head):
    l_val = []
    p = head
    while(p):
        l_val.insert(0,p.val)
        p = p.next

    p = head
    for i in l_val:
        p.val = i
        p = p.next
    return head
print_LN(reverse_linked_list1(head1))


"""
one turn solution
"""
def reverse_linked_list2(head):
    if head == None or head.next == None: #边界条件
        return head
    p = head #循环变量
    tmp_next = None #保存数据的临时变量
    newhead = None #新的翻转单链表的表头
    while p:
        tmp_next = p.next
        p.next = newhead
        newhead = p   # 更新 新链表的表头
        p = tmp_next
    return newhead

print_LN(reverse_linked_list2(head1))