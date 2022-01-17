
###  自己写的
#
# class Solution:
#     def twoSum (self, nums, target):
#         self.nums = nums
#         self.target = target
#         lenth = len(nums)
#         flag = []
#         # print(nums, target)
#         for i in range(lenth):
#             for j in range(i+1, lenth):
#                 if nums[i] + nums[j] == target:
#                     flag.append(i)
#                     flag.append(j)
#                     return [i,j]

### 首尾递进，只需要用到排序  复杂度  （nlogn）

# class Solution:
#     def twoSum(self, nums, target):
#         sorted_idx = sorted(range(len(nums)), key=lambda x: nums[x])
#
#         head = 0
#         tail = len(nums)-1
#         sumresult = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
#         while sumresult != target:
#             if sumresult < target:
#                 head += 1
#             elif sumresult > target:
#                 tail -= 1
#             sumresult = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
#
#         return [sorted_idx[head], sorted_idx[tail]]

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            num2 = target - num
            if num2 in hashmap:
                return [hashmap[num2], index]
            hashmap[num] = index
        return None


nums = [2, 7, 11, 15]
target = 9

test = Solution()
print(test.twoSum(nums, target))