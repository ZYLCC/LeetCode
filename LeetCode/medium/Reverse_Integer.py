'''https://leetcode-cn.com/problems/reverse-integer/'''


class Solution:
    def reverse(self, x):
        x_str = str(x)
        if x_str[0] == '-':
            t = x_str[len(x_str)-1:0:-1]
            t = '-' + t
        else:
            t = x_str[::-1]
        t = int(t)
        if (-(2**31) <= t <= (2**31)-1):
            return t
        else:
            return 0