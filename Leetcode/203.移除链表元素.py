#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


# @lc code=end

# 总结：
# 单链表基本结构为：ListNode(val, next)，其中val为当前节点的值，next为指向下一个节点的指针。
# 第一个节点为头节点，最后一个节点为尾节点，尾节点的next指针指向None。

# 解题思路：
# 预设一个虚拟头节点dummy，其next指针指向头节点head。
# 链表遍历的结构为：cur = dummy，while cur.next。从虚拟头节点开始遍历，直到当前节点的next指针为空。
# 如果cur.next.val == val，说明当前节点的下一个节点的值等于val，需要删除下一个节点。
# 为了删除节点，需要将当前节点的next指针指向下下个节点，即cur.next = cur.next.next。

# 复杂度分析：
# 时间复杂度：O(n)，其中n是链表的节点个数。需要遍历链表一次。
