#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


# @lc code=end

# 总结
# 1. 定义两个指针slow和fast，分别指向链表头节点
# 2. 遍历链表，当slow和fast相遇时，退出循环
# 3. 将fast指针指向链表头节点，继续遍历
# 4. 当slow和fast相遇时，返回slow指针
# 5. 如果slow和fast都为空时，返回None

# 关键点：
# 1. 当slow和fast相遇时，slow走了k步，fast走了2k步
# 2. 假设链表头节点到环的入口节点的距离为m，环的长度为n
# 3. 当slow和fast相遇时，slow走了m + x步，fast走了m + x + n步
# 4. 由于fast的速度是slow的两倍，所以有 2(m + x) = m + x + n
# 5. 所以有 m + x = n，即链表头节点到环的入口节点的距离等于slow和fast相遇点到环的入口节点的距离
# 6. 所以当slow和fast相遇时，将fast指针指向链表头节点，继续遍历，当slow和fast相遇时，返回slow指针

# 时间复杂度分析：
# 时间复杂度为O(n)，需要遍历整个链表
