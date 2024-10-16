#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        # 暴力法
        nums_ = []
        for num in nums:
            if num != val:
                nums_.append(num)
        nums[:] = nums_
        return len(nums)
    
    def removeElement2(self, nums: List[int], val: int) -> int:
        # 左闭右闭,左右指针
        left, right = 0, len(nums) - 1
        while left <= right:        # 终止条件是left>right，此时left=right是合法的
            if nums[left] != val:    
                left += 1           # 满足条件，保留元素，left指向下一个元素
            else:
                nums[left] = nums[right]        # 不满足条件，覆盖元素，right指向下一个元素
                right -= 1
        return left             # 最后left指向的是最后一个不等于val的元素的下一个元素，即数组长度
        
    def removeElement3(self, nums: List[int], val: int) -> int:
        # 快慢指针
        slow = 0 
        for fast in range(len(nums)):     # fast指针遍历数组
            if nums[fast] != val:         # 如果右指针满足条件，将右指针的值赋给左指针
                nums[slow] = nums[fast]
                slow += 1               # 左指针右移，准备下次赋值，并且索引+1等于满足条件的元素个数
        return slow
        
    def removeElement(self, nums: List[int], val: int) -> int:
        return self.removeElement3(nums, val)


# @lc code=end

'''
核心是用覆盖代替删除操作
左右指针：
    左指针指向需要移除的元素替换成替换成右指针指向元素，右指针左移
    左指针指向满足条件的元素，左指针左移
    最后左指针指向满足条件的下一个元素，即满足条件数组长度
快慢指针：
    快指针遍历数组，碰到满足条件元素就赋值给慢指针，并且慢指针向后移一位
'''