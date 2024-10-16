#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA


# @lc code=end

# 总结
# 1. 定义两个指针curA和curB，分别指向两个链表的头节点
# 2. 遍历两个链表，当curA和curB相等时，返回curA
# 3. 如果curA为空，则将curA指向headB，继续遍历
# 4. 如果curB为空，则将curB指向headA，继续遍历
# 5. 当curA和curB相等时，返回curA
# 6. 如果curA和curB都为空时，返回None

# 关键点：
# 相遇发生的总步数为 “较长链表的长度 + 较短链表到相交节点的长度”
# 为什么是较长链表的长度 + 较短链表到相交节点的长度？
# 链表 A 的长度为 m，其中从头节点到相交节点的长度为 x，相交部分的长度为 c。所以有：m = x + c。
# 链表 B 的长度为 n，其中从头节点到相交节点的长度为 y，相交部分的长度为 c。所以有：n = y + c。
# 当两个链表相遇时，
# curA 走了 x + c + y 步
# curB 走了 y + c + x 步
# 由于 x + c + y = y + c + x，所以 curA 和 curB 会在相交节点相遇。

# 时间复杂度分析：
# 时间复杂度为O(n)，需要遍历整个链表
