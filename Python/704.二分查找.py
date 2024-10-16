#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#


# @lc code=start
class Solution:
    # 写法一：左闭右闭[left, right]
    def search1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:  # <= 而不是 <，当范围缩小到只有一个元素时，left=right
            mid = (left + right) >> 1  # >> 等价于 //2
            if nums[mid] == target:
                return mid
            # 二分查找的核心思想，通过比较中间值和目标值的大小，来缩小查找范围
            # 如果中间值小于目标值，说明目标值在右边，所以 left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            # 如果中间值大于目标值，说明目标值在左边，所以 right = mid - 1
            else:
                right = mid - 1
        return -1

    # 写法二：左闭右开[left, right)
    def search2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # return self.search1(nums, target)
        return self.search2(nums, target)


# 总结
# 二分法使用条件：有序无重复数组
# 区间范围选择：左闭右闭[left, right]，左闭右开[left, right)，左开右闭(left, right]，左开右开(left, right)

# 第一种写法：左闭右闭[left, right]，
# left = 0, right = len(nums) - 1, while left <= right，此时left=right是合法的，右边界的值也要考虑
# nums[mid] < or > target，left = mid + 1 or right = mid - 1，target已经和mid比较过了，所以+1或-1


# 第二种写法：左闭右开[left, right)，
# left = 0, right = len(nums), while left < right，此时left=right是不合法的, 右边界的值不用考虑
# nums[mid] < target，left = mid + 1，target已经和mid比较过了，所以+1
# nums[mid] > target，right = mid，因为对于右开区间，右边界本身不在有效区间内，所以mid不用-1

# 复杂度分析
# 时间复杂度：O(logn)，每次查找都会将查找范围缩小一半
# 空间复杂度：O(1)，只需要常数空间存放若干变量

# @lc code=end
