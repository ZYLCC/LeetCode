'''https://leetcode-cn.com/problems/add-binary/'''

class Solution:
    def addBinary(self, a, b) -> str:
        # 内置函数
        # return bin(int(a, 2) + int(b, 2))[2:]  # 返回的二进制是“0b....”，所以分片[2:]

        # 模拟二进制求和
        n = max(len(a), len(b))
        a = [0] * (n - len(a) + 1) + list(map(int, a)) # 让a,b位数补齐，且前面均预留一位用于进位
        b = [0] * (n - len(b) + 1) + list(map(int, b))
        plus = [0 for _ in range(n + 1)]
        # plus = [a[i] + b[i] for i in range(n + 1)]
        for i in range(n, 0, -1):
            c = a[i] + b[i]
            if c + plus[i] <= 1:
                plus[i] += c
            elif c + plus[i] == 2:
                plus[i] = 0
                plus[i - 1] = 1
            elif c + plus[i] == 3:
                plus[i] = 1
                plus[i - 1] = 1

        re = ''.join(list(map(str, plus)))
        return re if plus[0] == 1 else re[1:]

test = Solution()
print(test.addBinary('11', '1'))
print(test.addBinary('1010', '1011'))








