'''https://leetcode-cn.com/problems/pascals-triangle/
https://leetcode-cn.com/problems/pascals-triangle-ii/'''


class Solution:
    # def generate(self, numRows: int):
        # triangle = []
        # line = []
        # for i in range(numRows):
        #     if i == 0:
        #         line = [1]
        #     else:
        #         line = self.eachline(line)
        #     triangle.append(line)
        # return triangle
    def getRow(self, rowIndex: int):
        line = []
        for i in range(rowIndex + 1):
            if i == 0:
                line = [1]
            else:
                line = self.eachline(line)
        return line

    def eachline(self, preline: list):
        n = len(preline)
        re = [1] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                continue
            elif i == n:
                continue
            else:
                re[i] = preline[i-1] + preline[i]
        return re


test = Solution()
# print(test.generate(5))
# print(test.generate(29))
# print(test.generate(1))
print(test.getRow(5))
print(test.getRow(29))
print(test.getRow(1))