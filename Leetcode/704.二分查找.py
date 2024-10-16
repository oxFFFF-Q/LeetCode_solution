#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#


# @lc code=start
class Solution:
        def search1(self, nums: List[int], target: int) -> int:
            # 暴力法
            for index,num in enumerate(nums):
                if num == target:
                    return index
            return -1

        def search2(self, nums: List[int], target: int) -> int:
            # 左闭右闭
            left, right = 0, len(nums)-1   # index范围是[nums最小值, nums最大值]
            while left <= right:           # 终止条件是left>right，此时left=right是合法的
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1         # 因为mid已经比较过了，所以-1
            return -1        
        
        def search3(self, nums: List[int], target: int) -> int:
            # 左闭右开
            left, right = 0, len(nums)   # index范围是[nums最小值, nums最大值+1)
            while left < right:         # 终止条件是left=right，此时left=right是不合法的
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid         # 因为mid不在有效区间内，没有比较过，所以不用-1
            return -1
        
        def search(self, nums: List[int], target: int) -> int:
            return self.search3(nums, target)
# @lc code=end


'''
	不断缩小左右边界来逼近目标值
左闭右开和左闭右闭：
        初始左右边界、
        循环结束条件(左右边界相等是否合法)
        和缩小后的右边界值都不同(mid是否已经比较)
'''

