class Solution:
    def reverseBetween(self, head, m, n):
        l = []
        p = head
        while(p):
            l.append(p.val)
            p = p.next
        m,n = m-1,n-1
        l1 = l[m:n+1]
        print(l1)
        l_re = l[:m] + l1[::-1] + l[n+1:]
        p = head
        for i in l_re:
            p.val = i
            p = p.next
        return head
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        