'''https://leetcode-cn.com/problems/valid-palindrome/'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for each in s:
            if each.isalpha() or each.isdigit():  # .isalnum() 直接判断是否为数字或字母
                tmp += each
        tmp = tmp.lower()
        return tmp == tmp[::-1]

        # 双指针
        # n = len(tmp)
        # for i in range(int(n/2+0.5)):  # 二分查找的 while left < right:的判断也行
        #     tail = n - i - 1
        #     if tmp[i] != tmp[tail]:
        #         return False
        # return True




test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))
print(test.isPalindrome("race a car"))
