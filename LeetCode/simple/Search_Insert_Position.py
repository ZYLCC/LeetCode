'''https://leetcode-cn.com/problems/search-insert-position/'''
class Solution:
    def searchInsert(self, nums, target) -> int:
        # 自己写的繁琐了, 多考虑了前边界的问题
        # nums.append(nums[-1]+10000)
        # if target <= nums[0]:
        #     return 0
        # else:
        #     for i in range(1, len(nums)):
        #         if nums[i-1] < target < nums[i] or target == nums[i]:
        #             return i

        # 简化版
        # for i in range(len(nums)):
        #     if target <= nums[i]:
        #         return i

        # 二分查找
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return left

test = Solution()
print(test.searchInsert([1,3,5,6],5))
print(test.searchInsert([1,3,5,6],2))
print(test.searchInsert([1,3,5,6],7))
