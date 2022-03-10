'''https://leetcode-cn.com/problems/length-of-last-word/comments/'''

class Solution:
    def lengthOfLastWord(self, s) -> int:
        s = list(s.split())
        return len(s[-1])


test = Solution()
print(test.lengthOfLastWord("Hello World"))
print(test.lengthOfLastWord("   fly me   to   the moon  "))
print(test.lengthOfLastWord("luffy is still joyboy"))