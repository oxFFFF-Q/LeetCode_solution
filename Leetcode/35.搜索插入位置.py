#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#


# @lc code=start
class Solution:
    # 左闭右闭[left, right]
    def searchInsert1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # 左闭右开[left, right)
    def searchInsert2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        # return self.searchInsert1(nums, target)
        return self.searchInsert2(nums, target)


# @lc code=end

# 总结
# 与704二分查找方法类似
# 唯一不同的是，当找不到目标值时，返回的是left，而不是-1

# 复杂度分析
# 时间复杂度：O(logn)，每次查找都会将查找范围缩小一半
# 如果使用循环遍历，时间复杂度为O(n)
