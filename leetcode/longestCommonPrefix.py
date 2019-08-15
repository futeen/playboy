'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明: 所有输入只包含小写字母 a-z 。

思路：
一共有N个字符串，要求公共前缀（需要是最长的）。此时假设已经知道前i+1
个字符串的最长公共前缀（dp[i]），此时再来一个字符串（即第i+2个字符串）
。如果第i+2个字符串不以dp[i]为前缀，就去掉dp[i]的最后一个字符串再试
一次，如果都去完了，那么最后结果就是空串。
'''


class Solution:
    # first solution
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        dp = [strs[0]] * len(strs)
        for i in range(1, len(strs)):
            # startswith() 方法用于检查字符串是否是以指定字符串开头
            while not strs[i].startswith(dp[i - 1]):
                dp[i - 1] = dp[i - 1][:-1]
            dp[i] = dp[i - 1]
        return dp[-1]

    # second solution(反向思维)
    def longestCommonPrefixt(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    print(Solution().longestCommonPrefixt(["llohell", "llofllow", "llojb"]))

