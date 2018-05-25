# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None


def link2int(l):
    l0 = str(l.val)
    while(l.next != None):
        l = l.next
        l0 += str(l.val)
    return l0

def reverse_str(s):
    print (s[::-1])
    return s[::-1]


def str2link(st):
    L = ListNode(int(st[0]))
    L_q = L
    for i in range(1,len(st)):
        L_h = ListNode(int(st[i]))
        L_q.next = L_h
        L_q = L_h
    return L


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_s = link2int(l1)
        l2_s = link2int(l2)
        l1_rev = reverse_str(l1_s)
        l2_rev = reverse_str(l2_s)
        res_int = int(l1_rev) + int(l2_rev)
        res_int_rev = reverse_str(str(res_int))

        res_s = str(res_int_rev)

        return str2link(res_s)


        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """