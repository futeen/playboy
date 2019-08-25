'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    #  first solution
    def addTwoNumbers(self, l1, l2):
        # 获得 l1 和 l2 的字符串表示, 因为题目说了l1和l2均非空，这里可以直接取val不会有问题
        num1Str, num2Str = str(l1.val), str(l2.val)
        while l1.next:
            num1Str += str(l1.next.val)
            l1 = l1.next
        while l2.next:
            num2Str += str(l2.next.val)
            l2 = l2.next
        # 得到 l1 和 l2 相加之和，因为在链表中数字是逆序存储，所以要反转一下
        sums = int(num1Str[::-1]) + int(num2Str[::-1])
        # 将 sums 转成题目中 linkedlist 所对应的表示形式
        sums = str(sums)[::-1]
        # dummy.next 作为返回结果
        dummy = head = ListNode(None)
        for i in range(len(sums)):
            head.next = ListNode(int(sums[i]))
            head = head.next
        return dummy.next

    # second solution
    def addTwoNumberst(self, l1, l2):
        if not l1 and not l2:
            return
        elif not (l1 and l2):  # l1 和 l2 其中一个是None
            return l1 or l2
        else:  # l1 和 l2都不是None
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.addTwoNumberst(l1.next, l2.next)
            else:
                l3 = ListNode(l1.val + l2.val - 10)
                l3.next = self.addTwoNumberst(l1.next, self.addTwoNumberst(l2.next, ListNode(1)))
        return l3

