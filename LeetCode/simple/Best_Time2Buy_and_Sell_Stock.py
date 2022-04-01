'''https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/'''

class Solution:
    def maxProfit(self, prices: list):
        # 算得上暴力法了，只不过给暴力法优化了下，不会超时

        # tmp = prices[:]
        # tmp.sort(reverse=True)
        # if prices == tmp:
        #     return 0
        # else:
        #     max_diff = 0
        #     # min_price = prices[0]
        #     min_index, i= 0, 0
        #     while i < len(prices) - 1:
        #         for j in range(i+1, len(prices)):
        #             diff = prices[j] - prices[i]
        #             if diff > max_diff:
        #                 max_diff = diff
        #             if prices[j] <= prices[i]:
        #                 i = j - 1  # 为了满足后面每一步外层循环都要+1
        #                 break
        #         i += 1
        #     return max_diff

        # dp
        # n = len(prices)
        # if n == 0: return 0
        # else:
        #     dp = [0] * n
        #     minprice = prices[0]
        #     for i in range(1, n):
        #         minprice = min(minprice, prices[i])
        #         dp[i] = max(dp[i - 1], prices[i] - minprice)  # dp转移方程，dp[i]代表前i天的最大利润
        #     return dp[-1]

        # dp, 优化空间后
        maxprofit = 0
        minprice = int(1e9)
        for each in prices:
            minprice = min(minprice, each)
            maxprofit = max(maxprofit, each - minprice)
        return maxprofit

test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))
print(test.maxProfit([7,6,4,3,1]))

