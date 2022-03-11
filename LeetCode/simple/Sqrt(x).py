'''https://leetcode-cn.com/problems/sqrtx/'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x - 1
        nums = [i+1 for i in range(x)]
        while l <= r:
            mid = (l + r) // 2
            product = nums[mid] * nums[mid]
            if product == x:
                return nums[mid]
            else:
                if product > x:
                    r = mid - 1
                else:
                    if product < x-1:
                        return nums[mid]
                    else:
                        l = mid + 1

test = Solution()
# print(test.mySqrt(4))
# print(test.mySqrt(8))
print(test.mySqrt(81))

