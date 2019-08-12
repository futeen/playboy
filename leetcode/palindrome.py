'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。


def f(text:str,max_len:'int>0'=80) ->str:
	"""这个是函数的帮助说明文档，help时会显示"""
    return True

函数声明中，text:str
text 是参数 :冒号后面  str是参数的注释。
如果参数有默认值，还要给注释，如下写。
max_len:'int>0'=80

->str 是函数返回值的注释。

这些注释信息都是函数的元信息，保存在f.__annotations__字典中、

需要注意，python对注释信息和f.__annotations__的一致性，
不做检查，不做强制，不做验证！什么都不做。
'''


class Solution:
    # first solution
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x != int(str(x)[::-1]):
            return False
        else:
            return False

    # second solution
    def isPalidromet(self, x: int) -> bool:
        # 负数肯定不是palindrome
        # 如果一个数字是一个正数，并且能被10整除，那它肯定也不是palindrome，因为首位肯定不是0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        # 此部分将数值倒转
        rev, y = 0, x
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return y == rev


print(Solution().way(1234))

