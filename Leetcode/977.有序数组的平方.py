#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#


# @lc code=start
class Solution:
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        # 暴力法, 时间复杂度O(nlogn)
        nums_abs = [abs(num) for num in nums]
        nums_abs.sort()  # 时间复杂度构成：O(n) * O(logn), 归并排序
        return [num**2 for num in nums_abs]

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n 
        left, right = 0, n-1  # 左闭右闭，从两端向中间零点靠拢
        for i in range(n-1, -1, -1):   # 从数组最大长度数值到0
            if abs(nums[left]) < abs(nums[right]):      
                ans[i] = nums[right] **2
                right -= 1
            else:
                ans[i] = nums[left] **2
                left += 1
        return ans
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return self.sortedSquares2(nums)

# @lc code=end


'''
左右指针：
    遍历数组长度次数，每次根据条件判断，执行什么操作，并向内收缩左指针或右指针
'''