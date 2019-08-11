'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:  # 如果是负数则取绝对值调用自身，最后将结果转为负数
            return -self.reverse(-x)
        res = 0
        while x:  # 每次得到最后一位数字，并将其作为结果中的当前最高位
            res = res * 10 + x % 10
            x //= 10
        return res if res <= 0x7fffffff else 0  # 如果溢出就返回0


print(Solution().reverse(77777777777))

