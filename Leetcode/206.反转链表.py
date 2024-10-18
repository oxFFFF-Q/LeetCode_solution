#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            # 保存当前节点的下一个节点
            next_node = current.next
            # 将当前节点的 next 指向 prev，实现反转
            current.next = prev
            # 移动 prev 和 current 指针
            prev = current
            current = next_node
        return prev
        
 
# @lc code=end

'''
206.反转链表
    暂存节点，prev和next交换
'''
