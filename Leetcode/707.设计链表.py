#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @lc code=start
# class MyLinkedList:

#     def __init__(self):

#     def get(self, index: int) -> int:
        

#     def addAtHead(self, val: int) -> None:


#     def addAtTail(self, val: int) -> None:


#     def addAtIndex(self, index: int, val: int) -> None:


#     def deleteAtIndex(self, index: int) -> None:


class MyLinkedList:
    
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy_head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = ListNode(val, cur.next)
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

