class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        else:
            maxnum = nums[0]
            cnt = 1
            for i in range(len(nums)):
                if maxnum != nums[i]:
                    maxnum = nums[i]
                    nums[cnt] = maxnum
                    cnt += 1
            return cnt



test = Solution()
print(test.removeDuplicates([1,1,2]))
print(test.removeDuplicates([]))
print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))