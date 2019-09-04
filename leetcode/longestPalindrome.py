'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb
'''


class Solution:
    def longestPalindrome(self, s):
        l = 0
        r = 0
        max_len = 0
        n = len(s)
        for i in range(n):
            # odd case:  'xxx s[i] xxx', such as 'abcdcba'
            for j in range(min(i + 1, n - i)):
                if s[i - j] != s[i + j]:
                    break
                if 2 * j + 1 > max_len:
                    max_len = 2 * j + 1
                    l = i - j
                    r = i + j
            # even case: 'xxx s[i] s[i+1] xxx', such as 'abcddcba'
            if i + 1 < n and s[i] == s[i + 1]:
                for j in range(min(i + 1, n - i - 1)):
                    if s[i - j] != s[i + 1 + j]:
                        break
                    if 2 * j + 2 > max_len:
                        max_len = 2 * j + 2
                        l = i - j
                        r = i + 1 + j
        return s[l:r + 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("abababscddf"))

