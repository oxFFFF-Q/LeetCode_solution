#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lc code=start
class Solution:
    # 左闭右闭[left, right]
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def searchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = searchLeft(nums, target)
        right = searchRight(nums, target)
        if left <= right:
            return [left, right]
        return [-1, -1]

    # 左闭右开[left, right)
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) >> 1
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def searchRight(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) >> 1
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return right

        left = searchLeft(nums, target)
        right = searchRight(nums, target)
        if left < right:
            return [left, right - 1]
        return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # return self.searchRange1(nums, target)
        return self.searchRange2(nums, target)


# @lc code=end

# 总结
# 二分查找的变种，分别查找左边界和右边界
# 需要注意的是：
# 当最初左右两半不存在目标值时，会发生越界
# 如果目标值恰好在中间，且仅出现一次，左边界会越界多计算一次left = mid + 1，恰好等于target
# 右边界会越界多计算一次right = mid - 1，恰好等于target
# 如果左右两半出现目标值，就会返回正确的左右边界
# 如果左右两半都不存在目标值，左右边界都会越界，所以此时left会大于right，返回[-1, -1]
