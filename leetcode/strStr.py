'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明: 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''


class Solution:
    # first solution
    def strStr(self, haystack, needle):
        return haystack.find(needle)

    # second solution
    # KMP 算法， 字符串越长，KMP相对于find()优势更明显
    # https://blog.csdn.net/v_july_v/article/details/7041827(KMP算法理解)
    def strStrt(self, haystack, needle):
        text, pattern = haystack, needle
        if not pattern:
            return 0
        lps = self.findLPS(pattern)  # longest proper prefix which is also suffix
        i, j = 0, 0  # idx for text and pattern
        res = -1
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                res = i - j
                return res
            elif i < len(text) and pattern[j] != text[i]:  # mismatch after j matches
                if j != 0:  # don't match lps[0..lps[j-1]] characters, they will match anyway
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def findLPS(self, pattern):
        length, lps = 0, [0]
        for i in range(1, len(pattern)):
            while length > 0 and pattern[length] != pattern[i]:
                length = lps[length - 1]
            if pattern[length] == pattern[i]:
                length += 1
            lps.append(length)
        return lps


if __name__ == "__main__":
    solution = Solution()
    print(solution.findLPS("abcdefcdbabababa"))

