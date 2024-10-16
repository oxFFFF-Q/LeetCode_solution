#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sum = 0
        res = float("inf")  # 初始化为正无穷
        for right in range(len(nums)):
            # 右指针右移，左指针不动，直到满足条件
            sum += nums[right]
            while sum >= target:
                # 比较当前子数组长度和之前的最小长度并更新
                res = min(res, right - left + 1)
                # 左指针右移，右指针不动，直到不满足条件
                sum -= nums[left]
                left += 1
        return 0 if res == float("inf") else res


# @lc code=end

# 总结：滑动窗口
# 核心还是双指针算法，两个指针构成一个窗口，在数组上滑动，通过移动左右指针来寻找符合条件的子数组。
# 重点是在数组中遍历移动终止位置时，如何移动起始位置，以及如何更新结果。
# 移动终止位置是一步操作，移动起始位置是一步操作，所以最多移动2n次。相当于只遍历了一次数组。
# 暴力法需要对于起始位置和终止位置各遍历一次，所以时间复杂度是O(n^2)。

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是数组的长度。指针 left 和 right 最多各移动 n 次。
