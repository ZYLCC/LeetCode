'''https://leetcode-cn.com/problems/valid-parentheses/'''


class Solution:
    def isValid(self, s):
        '''自己的思路'''
        # if len(s)/2 != len(s)//2:
        #     return False
        # else:
        #     if '()' not in s and '{}' not in s and '[]' not in s:
        #         return  False
        #     else:
        #         lists = list(s)
        #         while len(lists) > 1:
        #             flag = True
        #             idx = s.find('()')
        #             if idx >= 0:
        #                 lists.pop(idx)
        #                 lists.pop(idx)
        #                 s = ''.join(lists)
        #                 flag = False
        #             idx = s.find('[]')
        #             if idx >= 0:
        #                 lists.pop(idx)
        #                 lists.pop(idx)
        #                 s = ''.join(lists)
        #                 flag = False
        #             idx = s.find('{}')
        #             if idx >= 0:
        #                 lists.pop(idx)
        #                 lists.pop(idx)
        #                 s = ''.join(lists)
        #                 flag = False
        #             if flag:
        #                 break
        #         if len(lists) > 0:
        #             return False
        #         else:
        #             return True

        '''类似的思路但更简化'''
        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.replace('()','')
        #     s = s.replace('[]','')
        #     s = s.replace('{}','')
        # return s == ''

        '''栈'''
        dic = {'(': ')', '[': ']', '{': "}", '!': '!'}
        stack = ['!']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1

test = Solution()
print(test.isValid("(("))
print(test.isValid("("))
print(test.isValid("()"))
print(test.isValid("()[]{}"))
print(test.isValid("(]"))
print(test.isValid("([)]"))
print(test.isValid("{[]}"))



