#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            slow = prev.next
            fast = prev.next.next
            prev.next = fast
            slow.next = fast.next
            fast.next = slow
            prev = slow
        return dummy.next


# @lc code=end

# 总结
# 1. 定义一个dummy节点，用于存储头节点
# 2. 定义prev指针，指向dummy节点,代表前一个节点
# 3. 定义slow指针，指向prev.next,代表当前节点
# 4. 定义fast指针，指向slow.next,代表下一个节点
# 5. 每次交换slow和fast节点，更新prev指针
# 6. 当slow和fast都不为空时，继续交换
# 7. 返回dummy.next节点

# 时间复杂度分析：
# 时间复杂度为O(n)，需要遍历整个链表
