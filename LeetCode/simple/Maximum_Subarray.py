'''https://leetcode-cn.com/problems/maximum-subarray/'''

class Solution:
    def maxSubArray(self, nums) -> int:
        # 复杂度O(n^2)，超出力扣时间限制
        # max = float('-Inf')   #  不能取0，因为nums可能是全负数
        # for i in range(len(nums)):
        #     sum_ = 0
        #     for j in range(i, len(nums)):
        #         sum_ += nums[j]
        #         if sum_ >= max:
        #             max = sum_
        # return max

        # 复杂度O(n)，动态规划
        # max = float('-Inf')
        # temp = 0
        # for i in range(len(nums)):
        #     temp += nums[i]
        #     if temp > max:
        #         max = temp
        #     if temp < 0:
        #         temp = 0
        # return max

        # 动态规划1
        '''nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，
        和0比较是因为只要大于0，就可以相加构造最大子序和。如果小于0则相加为0，
        nums[i] = nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和
        和解法二其实是一个意思，更简便写法'''
        # for i in range(1, len(nums)):
        #     nums[i] = nums[i] + max(nums[i - 1], 0)
        # return max(nums)

        # 动态规划2
        # pre = 0
        # max_ = nums[0]
        # for each in nums:
        #     pre = max(pre + each, each)
        #     max_ = max(max_, pre)
        # return max_





test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(test.maxSubArray([1]))
print(test.maxSubArray([5,4,-1,7,8]))




