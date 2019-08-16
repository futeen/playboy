'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
 1.左括号必须用相同类型的右括号闭合。
 2.左括号必须以正确的顺序闭合。

注意：空字符串可被认为是有效字符串。

示例 :

输入: "()"
输出: true

输入: "()[]{}"
输出: true

输入: "([)]"
输出: false

输入: "{[]}"
输出: true
'''


class Solution:
    # first solution
    def isValid(self, s):
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace("[]", "").replace("()", "").replace("{}", "")
        return len(s) == 0

    # second solution
    def isValidt(self, s):
        leftP = "([{"
        rightP = ")]}"
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ")" and tmp != "(":
                    return False
                if char == "]" and tmp != "[":
                    return False
                if char == "}" and tmp != "{":
                    return False
        return stack == []


if __name__ == "__main__":
    print(Solution().isValidt("[(){}]"))

