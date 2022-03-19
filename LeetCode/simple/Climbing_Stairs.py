'''https://leetcode-cn.com/problems/climbing-stairs/'''

# class Solution:
#     # 加缓存装饰器
#     @functools.lru_cache(100)
#     def climbStairs(self, n: int) -> int:
#         # 斐波那契数列，递归
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else n


class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划 f(n) = f(n-1) + f(n-2)
        p, q, r = 0, 0, 1
        for _ in range(n):
            p = q
            q = r
            r = p + q
        return r

test = Solution()
print(test.climbStairs(1))
print(test.climbStairs(4))
print(test.climbStairs(5))
print(test.climbStairs(45))
