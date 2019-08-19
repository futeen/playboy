'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

说明: 为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''


class Solution:
    # first solution
    def removeDuplicates(self, nums):
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx + 1]:  # 若相等pop掉当前值
                nums.pop(idx)
            else:  # 否则move到下一位置继续做判断
                idx += 1
        return len(nums)

    # second solution
    '''
    上面的方式有一个缺陷：我们的时间复杂度是O(N^2), 因为每一次pop操作
    我们都需要将被删除元素后面的所有元素向前移动一格，如何优化？
    其实只要不停的向下遍历，同时自增的分配不重复的值给前面的位置即可。
    '''

    def removeDuplicatest(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            # 第一位自然不可能重复（同时保证数组不越界）
            if idx < 1 or num != nums[idx - 1]:
                nums[idx] = num
                idx += 1
        return idx

    # third solution
    '''
    如果允许要给作品作者组多可以得到两份奖品，该如何处理？
    此时可以允许有两个重复值，超过两次重复就不行了。
    '''

    def removeDuplicatesh(self, nums: List[int]) -> int:
        idx = 0
        for num in nums:
            if idx < 2 or num != nums[idx - 2]:
                nums[idx] = num
                idx += 1
        return idx

    # fourth -> leedcode 83
    '''
    链表排序移除重复元素
    '''
    def deleteDuplicates(self, head):
        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return dummy

    # fifth -> leetcode 82
    '''
    想让最终的链表中只留下之前没有重复的元素，
    可用prev指针指向前面的元素，方便进行比较
    '''
    def deleteDuplicatest(self, head):
        dummy = prev = cur = ListNode(None)
        while head:
            while head and ((head.val == prev.val) or (head.next and head.next.val == head.val)):
                prev = head
                head = head.next
            cur.next = head
            cur = cur.next
            if head:
                head = head.next
        return dummy.next

