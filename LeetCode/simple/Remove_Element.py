class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        else:
            cnt = 0
            n = len(nums)
            for i in range(n):
                if nums[i] != val:
                    nums[cnt] = nums[i]
                    cnt += 1
        # print(nums[:cnt])
        return cnt


test = Solution()
print(test.removeElement(nums = [3,2,2,3], val = 3))
print(test.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))