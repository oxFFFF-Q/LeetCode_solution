#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#


# @lc code=start
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next    # 删除节点=将当前节点的next指向下下个节点
            else:
                cur = cur.next
        return dummy.next


# @lc code=end

'''
删除节点=将当前节点的next指向下下个节点
'''
