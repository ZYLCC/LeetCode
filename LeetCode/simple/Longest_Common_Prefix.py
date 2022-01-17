'''https://leetcode-cn.com/problems/longest-common-prefix/'''


class Solution:
    def longestCommonPrefix(self, strs):
        '''''自己写的'''''
        # maxPre = ['']*200
        # flag = False
        # if len(strs) == 1:
        #     maxPre = strs[0]
        # else:
        #     for j in range(min([len(each) for each in strs])):
        #         for i in range(len(strs) - 1):
        #             if strs[i][j] == strs[i+1][j]:
        #                 maxPre[j] = strs[i][j]
        #             else:
        #                 maxPre[j] = ''
        #                 flag = True
        #                 break
        #         if flag:
        #             break
        # maxPre = ''.join(maxPre)
        # print(maxPre)
        # return maxPre

        '''先根据字典排序，再判断首尾'''
        # strs.sort()
        # maxPre = ''
        # for i in range(min(len(strs[0]), len(strs[-1]))):
        #     if strs[0][i] == strs[-1][i]:
        #         maxPre += strs[0][i]
        #     else:
        #         break
        # # print(maxPre)
        # return maxPre

        '''利用min，max得到上述排序方法的首尾'''
        # maxPre = ''
        # head = min(strs)
        # tail = max(strs)
        # for i in range(min(len(head), len(tail))):
        #     if head[i] == tail[i]:
        #         maxPre += head[i]
        #     else:
        #         break
        # # print(maxPre)
        # return maxPre

        '''利用zip函数“解压”strs成二维数组，利用set合并相同的'''
        maxPre = ''
        temp = list(map(set, zip(*strs)))

        for each in temp:
            if len(each) > 1:
                break
            maxPre += list(each)[0]
        print(maxPre)
        return maxPre

test = Solution()
test.longestCommonPrefix(["flower","flow","flight"])
test.longestCommonPrefix(["dog","racecar","car"])
test.longestCommonPrefix(["sss"])
test.longestCommonPrefix(["ab", "a"])
test.longestCommonPrefix(["abab","aba",""])
test.longestCommonPrefix(["flower","flow","flight"])

