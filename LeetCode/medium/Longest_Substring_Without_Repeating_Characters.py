'''https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/'''

class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        # tmp = []
        # maxlength = 0
        # for each in s:
        #     if each not in tmp:
        #         tmp.append(each)  # 将未出现的按顺序写入tmp
        #         if len(tmp) > maxlength:
        #             maxlength = len(tmp)
        #     else:  # 将和each重复的字符及左边的所有字符删除，并将each写入tmp最右边
        #         tmp = tmp[tmp.index(each) + 1:]
        #         tmp.append(each)
        # return maxlength


        # 官方题解，思想类似
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans








test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))
print(test.lengthOfLongestSubstring("dvdf"))
print(test.lengthOfLongestSubstring("bbbbb"))
print(test.lengthOfLongestSubstring("pwwkew"))
print(test.lengthOfLongestSubstring("pwke"))
print(test.lengthOfLongestSubstring("a"))
print(test.lengthOfLongestSubstring(""))
print(test.lengthOfLongestSubstring("aabaab!bb"))
































