'''https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/'''

class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        #
        tmp = []
        maxlength = 0
        for each in s:
            if each not in tmp:
                tmp.append(each)
                if len(tmp) > maxlength:
                    maxlength = len(tmp)
            else:
                tmp = tmp[tmp.index(each)+1:]
                tmp.append(each)
        return maxlength





test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))
print(test.lengthOfLongestSubstring("dvdf"))
print(test.lengthOfLongestSubstring("bbbbb"))
print(test.lengthOfLongestSubstring("pwwkew"))
print(test.lengthOfLongestSubstring("pwke"))
print(test.lengthOfLongestSubstring("a"))
print(test.lengthOfLongestSubstring(""))
print(test.lengthOfLongestSubstring("aabaab!bb"))
































