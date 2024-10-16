#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # 如果矩阵为空，返回空数组
        if not matrix:
            return res
        # 初始化上下左右指针
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        # 左闭右闭
        while top <= bottom and left <= right:
            # 从左到右
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            # 从上到下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            # 从右到左，注意判断是否越界，防止再次处理已经处理过的行
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            # 从下到上，注意判断是否越界，防止再次处理已经处理过的列
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res


# @lc code=end


# 总结：
# 对比59螺旋矩阵II，这里是输出螺旋矩阵
# 基本思路类似，还是上下左右四个指针，固定左闭右闭
# 另外需要注意判断是否越界，防止再次处理已经处理过的行或列

# 复杂度分析：
# 时间复杂度：O(m*n)，m和n分别是矩阵的行数和列数
