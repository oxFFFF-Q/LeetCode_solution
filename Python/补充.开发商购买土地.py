import time


def calculate_min_difference_brute_force(n, m, vec):
    """
    暴力法：遍历所有可能的横向和纵向切割位置，计算最小的土地总价值差异。
    """
    total_sum = sum(sum(row) for row in vec)
    result = float("inf")

    # 横向切割
    for i in range(1, n):
        region1 = sum(sum(vec[k]) for k in range(i))
        region2 = total_sum - region1
        result = min(result, abs(region1 - region2))

    # 纵向切割
    for j in range(1, m):
        region1 = sum(sum(vec[k][l] for l in range(j)) for k in range(n))
        region2 = total_sum - region1
        result = min(result, abs(region1 - region2))

    return result


def calculate_min_difference_optimized(n, m, vec):
    """
    优化暴力法：在每次遍历时同时统计累积和，避免重复计算。
    """
    total_sum = sum(sum(row) for row in vec)
    result = float("inf")
    
    # 行切分
    row_sum = 0
    for i in range(n):
        row_sum += sum(vec[i])
        result = min(result, abs(total_sum - 2 * row_sum))

    # 列切分
    col_sum = 0
    for j in range(m):
        col_sum += sum(vec[i][j] for i in range(n))
        result = min(result, abs(total_sum - 2 * col_sum))

    return result


def calculate_min_difference_prefix_sum(n, m, vec):
    """
    前缀和法：使用前缀和数组进行计算，提高查询效率。
    """
    total_sum = sum(sum(row) for row in vec)

    # 计算行和列的前缀和
    row_prefix_sum = [0] * n
    col_prefix_sum = [0] * m

    for i in range(n):
        row_prefix_sum[i] = sum(vec[i]) + (row_prefix_sum[i - 1] if i > 0 else 0)

    for j in range(m):
        col_prefix_sum[j] = sum(vec[i][j] for i in range(n)) + (col_prefix_sum[j - 1] if j > 0 else 0)

    result = float("inf")

    # 横向切割
    for i in range(n - 1):
        row_diff = abs(total_sum - 2 * row_prefix_sum[i])
        result = min(result, row_diff)

    # 纵向切割
    for j in range(m - 1):
        col_diff = abs(total_sum - 2 * col_prefix_sum[j])
        result = min(result, col_diff)

    return result


# 测试用例
def run_tests():
    """
    运行暴力法、优化暴力法和前缀和法，并输出通过/未通过测试用例数量和耗时。
    """
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
        (3, 3, [[1, 2, 1], [2, 100, 2], [1, 2, 1]], 104),
    ]

    # 统计通过的用例数量和总耗时
    brute_force_passed = 0
    optimized_passed = 0
    prefix_sum_passed = 0
    brute_force_time = 0.0
    optimized_time = 0.0
    prefix_sum_time = 0.0

    for idx, (n, m, vec, expected) in enumerate(test_cases):
        # Test brute-force method
        start_time = time.perf_counter()
        result = calculate_min_difference_brute_force(n, m, vec)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        brute_force_time += elapsed_time
        if result == expected:
            brute_force_passed += 1

        # Test optimized method
        start_time = time.perf_counter()
        result = calculate_min_difference_optimized(n, m, vec)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        optimized_time += elapsed_time
        if result == expected:
            optimized_passed += 1

        # Test prefix sum method
        start_time = time.perf_counter()
        result = calculate_min_difference_prefix_sum(n, m, vec)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        prefix_sum_time += elapsed_time
        if result == expected:
            prefix_sum_passed += 1

    # 输出结果
    total_tests = len(test_cases)
    print(f"Brute-force: {brute_force_passed}/{total_tests} tests passed, time: {brute_force_time:.6f} seconds")
    print(f"Optimized: {optimized_passed}/{total_tests} tests passed, time: {optimized_time:.6f} seconds")
    print(f"Prefix sum: {prefix_sum_passed}/{total_tests} tests passed, time: {prefix_sum_time:.6f} seconds")


if __name__ == "__main__":
    run_tests()


'''
暴力法
    需要遍历所有行和列，每次需要 O(n * m)
优化的暴力法
    每次遍历时累积行或列的总和，避免重复计算，总共O(n * m)
前缀法
    提前计算每一行和每一列的累积和，总共O(n * m)
'''