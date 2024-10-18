#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#


# @lc code=start
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(0)  # 定义一个虚拟头节点
        self.size = 0
    
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        cur = self.dummy_head
        for _ in range(index+1):  # 从虚拟头节点开始, 所以是index+1
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.dummy_head
        cur.next = ListNode(val=val, prev=self.dummy_head, next=self.dummy_head.next)
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val=val, prev=cur, next=None)
        self.size += 1
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = ListNode(val=val, prev=cur, next=cur.next)
        self.size += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next    # 如果删除的是最后一个节点, cur.next.next=None
        if cur.next:                # 如果删除的不是最后一个节点       
            cur.next.prev = cur     # 将下一个节点的prev指向当前节点
        self.size -= 1
        
# @lc code=end
'''
		链表一般开始于虚拟头节点，因为需要通过next进行处理第一个节点
        链表最后一个节点的next以及n个next都为Null, 因为不存在
'''
