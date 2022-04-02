'''https://leetcode-cn.com/problems/single-number/'''

from functools import reduce
class Solution:
    def singleNumber(self, nums) -> int:

        # 异或运算  a⊕0=a，a⊕a=0  满足交换律和结合律
        # re = 0
        # for each in nums:
        #     re ^= each
        # return  re

        # # 可用reduce函数 reduce(function, iterable[, initializer]) python3需要导包
        # return reduce(lambda x, y: x ^ y, nums)

        # 一般方法
        tmp = []
        for each in nums:
            if each in tmp:
                tmp.remove(each)
            else:
                tmp.append(each)
        return tmp[0]



test = Solution()
print(test.singleNumber([2,2,1]))
print(test.singleNumber([4,1,2,1,2]))
