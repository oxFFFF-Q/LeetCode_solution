# @before-stub-for-debug-begin
from python3problem206 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

        # dummy = ListNode()
        # cur = head
        # while cur:
        #     next = cur.next
        #     cur.next = dummy.next
        #     dummy.next = cur
        #     cur = next
        # return dummy.next


# @lc code=end

# 总结
# 方式一：迭代
# 1. 定义两个指针prev和cur，分别指向前一个节点和当前节点
# 2. 遍历链表，每次将当前节点的next指向前一个节点
# 3. 更新prev和cur指针，继续遍历
# 4. 当cur指向None时，遍历结束，返回prev指针
# 方式二：头插法
# 1. 定义一个dummy节点，用于存储反转后的链表
# 2. 遍历链表，每次将当前节点插入到dummy节点的后面
# 3. 更新cur指针，继续遍历

# 时间复杂度分析：
# 时间复杂度为O(n)，需要遍历整个链表
