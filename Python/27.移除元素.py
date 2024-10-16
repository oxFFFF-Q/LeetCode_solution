#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:
    # 左闭右开[left, right)
    def removeElement1(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return left

    # 左闭右闭[left, right]
    def removeElement2(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left

    # 补充：快慢指针
    def removeElement3(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

    def removeElement(self, nums: List[int], val: int) -> int:
        # return self.removeElement1(nums, val)
        # return self.removeElement2(nums, val)
        return self.removeElement3(nums, val)


# @lc code=end

# 总结
# 与二分查找不同，这里不是通过mid和target的比较来缩小查找范围
# 而是通过left和right指针，实现通过覆盖的方式来移除元素
# 关键点在于，数组在内存空间中是连续存储的，所以在删除或插入元素时，会导致后续元素的移动
# 所以如果通过暴力法，每次删除元素后，都需要将后续元素向前移动，极端情况下，数组中全部元素都是要删除的元素，时间复杂度为O(n^2)
# 而通过左右指针，只需要一次遍历，时间复杂度为O(n)

# 补充：快慢指针，
# 与左右指针不同，快指针用于遍历数组，慢指针用来记录不等于val的元素
# 即快指针把找到的不等于val的元素，放到慢指针的位置上
# 在val较多的情况下，左右指针需要更多覆盖操作，而快慢指针只需要一次遍历

# 复杂度分析
# 两种指针方法的时间复杂度都是O(n)
# 暴力法的时间复杂度为O(n^2)
