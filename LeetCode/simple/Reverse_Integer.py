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


test = Solution()
print(test.reverse(1563847412))
# print(test.reverse(-123))
# print(test.reverse(120))
