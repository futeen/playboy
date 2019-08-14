'''
罗马数字包含以下七种字符： I、 V、 X、 L、C、D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1；12 写做 XII ，即为 X + II ； 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边，但也存在特例。例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9；
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90；
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900；
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:
输入: 3
输出: "III"

示例 2:
输入: 4
输出: "IV"

示例 3:
输入: 9
输出: "IX"

示例 4:
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例 5:
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

思路：数字转罗马
以整数 3568 为例，3568 的对应罗马数字为：MMMDLXVIII

第一次 for 循环 ————> symbol = 'M' val = 1000 , num >= val成立，进入 while 循环：
	第一次 while 循环：
		将 'M' 拼接到 roman 中， num 减去当前 val ，此时 roman 为 'M',num 为 2568
	第二次 while 循环：
		将 'M' 拼接到 roman 中，num 减去当前 val ，此时 roman 为 'MM',num 为 1568
	第三次 while 循环：
		将 'M' 拼接到 roman 中，num 减去当前 val ，此时 roman 为 'MMM',num 为 568 					num >= val 不成立，退出 while 循环。
第二次 for 循环 ————> symbol = 'CM' val = 900 , num >= val不成立，不能进入 while 循环：
第三次 for 循环 ————> symbol = 'D' val = 500 , num >= val成立，进入 while 循环：
	第一次 while 循环：
    	将 'D' 拼接到 roman 中， num 减去当前 val ，此时 roman 为 'MMMD',num 为 68
        num >= val 不成立，退出 while 循环。
第四次 for 循环 ————> symbol = 'CD' val = 400 , num >= val不成立，不能进入 while 循环：
…………
第七次 for 循环 ————> symbol = 'L' val = 50 , num >= val成立，进入 while 循环：
	第一次 while 循环：
    	将 'L' 拼接到 roman 中， num 减去当前 val ，此时 roman 为 'MMMDL',num 为 18
        num >= val 不成立，退出 while 循环。
…………依次执行后得出结果为 MMMDLXVIII 。
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        roman = ""
        # 因为dict本身是无序的，这里做了一个排序的操作，否则可能会出现IIII这种状况
        for symbol, val in sorted(lookup.items(), key=lambda t: t[1])[::-1]:
            while num >= val:
                roman += symbol
                num -= val
        return roman

    def romanToInt(self, s: str) -> int:
        # 初始化了一个一一对应的map，方便后面取出符号。
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s)):
            if i > 0 and lookup[s[i]] > lookup[s[i-1]]:
                res += lookup[s[i]] - 2*lookup[s[i-1]]
            else:
                res += lookup[s[i]]
        return res


print(Solution().romanToInt('MIV'))

