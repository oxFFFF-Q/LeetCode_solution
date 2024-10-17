#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#


# @lc code=start
# class Solution:

class Solution:
    def generateMatrix1(self, n: int) -> List[List[int]]:
        # 左闭右闭, if-else判断边界
        res = [[0]*n for _ in range(n)]
        left, right, top, bottom = 0,n-1,0,n-1
        num = 1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                res[top][i] = num
                num += 1
            top += 1
            for i in range(top,bottom+1):
                res[i][right] = num
                num += 1
            right -= 1
            for i in range(right,left-1,-1):
                res[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom,top-1,-1):
                res[i][left] = num
                num += 1
            left += 1
        return res
                   
    def generateMatrix2(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
        row, col, direction = 0, 0, 0
        num = 1

        for _ in range(n * n):
            res[row][col] = num
            num += 1
            # 计算下一个位置
            next_row, next_col = row + directions[direction][0], col + directions[direction][1]
            # 如果越界或者已经填充，改变方向
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or res[next_row][next_col] != 0:
                direction = (direction + 1) % 4  # 顺时针改变方向
                next_row, next_col = row + directions[direction][0], col + directions[direction][1]
            row, col = next_row, next_col
        
        return res
    
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        # return self.generateMatrix1(n)
        return self.generateMatrix2(n)



# @lc code=end

'''
59.螺旋矩阵
	两对双指针，需要注意边界条件和rang终点不包含
	时间复杂度最优O(n^2), 因为一共n^2个元素，至少n^2次操作
    根据螺旋矩阵方向特性，简化代码避免if-else
'''
