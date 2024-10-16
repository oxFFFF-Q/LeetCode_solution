"""
【题目描述】

在一个城市区域内，被划分成了n * m个连续的区块，每个区块都拥有不同的权值，代表着其土地价值。目前，有两家开发公司，A 公司和 B 公司，希望购买这个城市区域的土地。

现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。

然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且每个子区域都必须包含一个或多个区块。

为了确保公平竞争，你需要找到一种分配方式，使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。

注意：区块不可再分。

【输入描述】

第一行输入两个正整数，代表 n 和 m。

接下来的 n 行，每行输出 m 个正整数。

输出描述

请输出一个整数，代表两个子区域内土地总价值之间的最小差距。

【输入示例】

3 3 1 2 3 2 1 3 1 2 3

【输出示例】

0

【提示信息】

如果将区域按照如下方式划分：

1 2 | 3 2 1 | 3 1 2 | 3

两个子区域内土地总价值之间的最小差距可以达到 0。

【数据范围】：

1 <= n, m <= 100；
n 和 m 不同时为 1。
#
"""


def calculate_min_difference(n, m, vec):
    total_sum = sum(sum(row) for row in vec)

    # 计算横向和纵向的累积和
    horizontal = [sum(vec[i]) for i in range(n)]
    vertical = [sum(vec[i][j] for i in range(n)) for j in range(m)]

    result = float("inf")

    # 横向分割
    horizontal_cut = 0
    for i in range(n):
        horizontal_cut += horizontal[i]
        result = min(result, abs(total_sum - 2 * horizontal_cut))
        if result == 0:
            return 0  # 如果找到了差值为0的情况，提前返回

    # 纵向分割
    vertical_cut = 0
    for j in range(m):
        vertical_cut += vertical[j]
        result = min(result, abs(total_sum - 2 * vertical_cut))
        if result == 0:
            return 0  # 如果找到了差值为0的情况，提前返回

    return result


# 测试示例
def main():
    test_cases = [
        # 示例1: 基础测试，矩阵中的值相对平衡
        (3, 3, [[1, 2, 3], [2, 1, 3], [1, 2, 3]], 0),
        # 示例2: 单一行的矩阵
        (1, 4, [[1, 3, 2, 4]], 2),
        # 示例3: 单一列的矩阵
        (4, 1, [[1], [2], [3], [4]], 2),
        # 示例4: 不均匀分布的矩阵
        (2, 3, [[1, 1, 100], [1, 1, 1]], 97),
        # 示例5: 较大矩阵，检查性能
        (3, 3, [[1, 2, 1], [2, 100, 2], [1, 2, 1]], 104),  # 修正后的预期结果为104
    ]

    for idx, (n, m, vec, expected) in enumerate(test_cases):
        result = calculate_min_difference(n, m, vec)
        print(f"测试用例 {idx + 1}: 计算结果 = {result}, 预期结果 = {expected}")
        assert result == expected, f"测试用例 {idx + 1} 失败"


if __name__ == "__main__":
    main()


# 总结：
# 对比区间和是一维前缀和，这里是二维前缀和
# 需要注意