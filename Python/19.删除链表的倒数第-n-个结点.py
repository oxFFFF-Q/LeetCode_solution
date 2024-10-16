#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


# @lc code=end

# 总结
# 1. 定义一个dummy节点，用于存储头节点
# 2. 定义slow和fast指针，用于遍历链表
# 3. fast指针先走n+1步，然后slow指针开始走
# 4. 当fast指针走到链表尾部时，slow指针指向要删除节点的前一个节点
# 5. 删除slow.next节点，返回dummy.next节点

# 时间复杂度分析：
# 时间复杂度为O(n)，需要遍历整个链表
