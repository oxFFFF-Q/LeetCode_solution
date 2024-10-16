#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#


# @lc code=start
class Solution:
    # 左闭右闭[left, right]
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                ans[i] = nums[right] * nums[right]
                right -= 1
            else:
                ans[i] = nums[left] * nums[left]
                left += 1
        return ans

    # 左闭右开[left, right)
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left, right = 0, n
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right - 1]):
                ans[i] = nums[right - 1] * nums[right - 1]
                right -= 1
            else:
                ans[i] = nums[left] * nums[left]
                left += 1
        return ans

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return self.sortedSquares1(nums)
        return self.sortedSquares2(nums)


# @lc code=end

# 总结
# 通过左右指针，实现从两端到中间的有序平方数组

# 复杂度分析
# 时间复杂度：O(n)，只需要一次遍历
