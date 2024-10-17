#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        # 暴力法
        lengeth = len(nums)
        result = float("inf")
        for i in range(lengeth):
            sum = 0
            for j in range(i, lengeth):
                sum += nums[j]
                if sum >= target:
                    result = min(result,j-i+1)
                    break
        return 0 if result == float("inf") else result
    
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        # 滑动窗口
        right, left = 0, 0
        sum = 0
        result = float("inf")
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:      # 当满足条件时
                result = min(result, right - left + 1)   # 更新结果   
                sum -= nums[left]                        # 去除左边元素
                left += 1                                # 左指针右移
        return 0 if sum==float("inf") else result
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return self.minSubArrayLen2(target, nums)

# @lc code=end

'''
209.滑动窗口
	通过左右两个边界圈定一个窗口，右边界从左到右遍历数组，同时判断窗口内元素是否满足条件，如果满足则保存并比较窗口内元素，并且左边界右移一位，右边界继续遍历
    暴力法需要嵌套两层循环O(n^2), 滑动窗口仅需要一遍遍历O(n)
'''