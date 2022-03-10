'''https://leetcode-cn.com/problems/plus-one/comments/'''


class Solution:
    def plusOne(self, digits):
        s = ''
        for each in digits:
            s += str(each)
        s = int(s) + 1
        return [int(x) for x in str(s)]

test = Solution()
print(test.plusOne([1,2,3]))
print(test.plusOne([4,3,2,1]))
print(test.plusOne([0]))
print(test.plusOne([9]))