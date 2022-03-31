'''https://leetcode-cn.com/problems/merge-sorted-array/'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 直接排序
        nums1[m:] = nums2
        nums1.sort()

        # 双指针 需要额外空间tmp
        # i, j= 0, 0
        # tmp = []
        # while i < m or j < n:
        #     if i == m:
        #         tmp.append(nums2[j])
        #         j += 1
        #     elif j == n:
        #         tmp.append(nums1[i])
        #         i += 1
        #     elif nums1[i] < nums2[j]:
        #         tmp.append(nums1[i])
        #         i += 1
        #     elif nums2[j] <= nums1[i]:
        #         tmp.append(nums2[j])
        #         j += 1
        #
        # nums1[:] = tmp
        # return None

        # 双逆指针 不需要额外空间，直接从尾到头进行覆盖nums1
        i, j = m - 1, n - 1

        while i > -1 or j > -1:
            if i == -1:
                nums1[i+j+1] = nums2[j]
                j -= 1
            elif j == -1:
                nums1[i+j+1] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        return None



test = Solution()
test.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
test.merge([1], 1, [], 0)
test.merge([0],  0, [1], 1)
