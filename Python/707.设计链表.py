#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

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
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        self.size += 1
        cur = self.head
        node = ListNode(val)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        for _ in range(index - 1):
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        cur = self.head
        if index == 0:
            self.head = self.head.next
            return
        for _ in range(index - 1):
            cur = cur.next
        cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
