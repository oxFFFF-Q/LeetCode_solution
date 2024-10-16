#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化矩阵，全部为0
        res = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1
        # 左闭右闭
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res


# @lc code=end

# 总结：
# 对比双指针算法，这里可以看成两对双指针，分别是上下指针和左右指针
# 相当于从一维窗口变成了二维窗口
# 循环不变量：上下指针和左右指针的格式，这里固定为左闭右闭

# 复杂度分析：
# 时间复杂度：O(n^2)，其中 n 是输入参数 n。
