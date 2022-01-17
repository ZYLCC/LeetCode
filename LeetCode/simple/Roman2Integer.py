'''https://leetcode-cn.com/problems/roman-to-integer/'''

class Solution:
    def romanToInt(self, str):
        str += ' '
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000, ' ': 0}
        special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        re = 0
        i = 0

        while (str[i] != ' '):
            if str[i]+str[i+1] in special:
                re += special[str[i]+str[i+1]]
                i += 2
            else:
                re += dic[str[i]]
                i += 1
        # print(re)
        return re


test = Solution()
test.romanToInt('III')
test.romanToInt('IV')
test.romanToInt('IX')
test.romanToInt('LVIII')
test.romanToInt('MCMXCIV')

