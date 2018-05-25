def reverse(self, x):
        flag = 0

        if (abs(x)> (2**31)-1):
            return 0

        if x < 0:
            flag = 1
            x  = -1 * x

        s_n = str(x)[::-1]
        r_n = int(s_n)

        if (abs(r_n)> (2**31)-1):
            return 0

        return r_n * ( (-1)**flag )