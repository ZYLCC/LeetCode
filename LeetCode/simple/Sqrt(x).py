'''https://leetcode-cn.com/problems/sqrtx/'''

class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找
        if x == 0:
            return x
        elif 0 < x < 4:
            return 1
        elif 4 <= x <= 8:
            return 2
        elif 9 <= x < 16:
            return 3
        else:
            l = 0
            r = x // 3
            re = -1
            while l <= r:
                mid = (l + r) // 2
                if mid * mid <= x:
                    re = mid
                    l = mid + 1
                else:
                    r = mid - 1
        return re








test = Solution()
print(test.mySqrt(4))
print(test.mySqrt(10))
print(test.mySqrt(0))
print(test.mySqrt(8))
print(test.mySqrt(81))
print(test.mySqrt(145))
print(test.mySqrt(10000))
print(test.mySqrt(10001))
print(test.mySqrt(2147395599))


