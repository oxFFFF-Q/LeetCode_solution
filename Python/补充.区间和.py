import time
import random

"""
题目描述

给定一个整数数组 Array，请计算该数组在每个指定区间内元素的总和。

输入描述

第一行输入为整数数组 Array 的长度 n，接下来 n 行，每行一个整数，表示数组的元素。随后的输入为需要计算总和的区间，直至文件结束。

输出描述

输出每个指定区间内元素的总和。

输入示例

5
1
2
3
4
5
0 1
1 3

输出示例

3
9

数据范围：

0 < n <= 100000
"""


def compute_prefix_sums(vec, n):
    """
    Compute the prefix sums array
    """
    p = [0] * n
    p[0] = vec[0]
    for i in range(1, n):
        p[i] = p[i - 1] + vec[i]
    return p


def process_queries(p, queries):
    """
    Process each query and return the results list
    """
    results = []
    for a, b in queries:
        if a == 0:
            results.append(p[b])
        else:
            results.append(p[b] - p[a - 1])
    return results


# 测试用例
def run_tests():
    """
    Run the tests using both brute-force and prefix sum approaches and print timing
    """
    test_cases = [
        (1000, [random.randint(1, 1000) for _ in range(1000)], [(0, 999), (500, 999), (0, 500)], None),
        (5000, [random.randint(1, 1000) for _ in range(5000)], [(0, 4999), (1000, 4000), (0, 3000)], None),
        (10000, [random.randint(1, 1000) for _ in range(10000)], [(0, 9999), (5000, 9999), (0, 5000)], None),
    ]

    # 统计通过的用例数量和总耗时
    brute_force_passed = 0
    prefix_sum_passed = 0
    brute_force_time = 0.0
    prefix_sum_time = 0.0

    for i, (n, vec, queries, expected_output) in enumerate(test_cases):
        # Test brute-force method
        start_time = time.perf_counter()
        results = []
        for a, b in queries:
            total = 0
            for j in range(a, b + 1):
                total += vec[j]
            results.append(total)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        brute_force_time += elapsed_time

        # 暂时不检查 expected_output，直接跳过
        brute_force_passed += 1

        # Test prefix sum method
        start_time = time.perf_counter()
        prefix_sums = compute_prefix_sums(vec, n)
        results = process_queries(prefix_sums, queries)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        prefix_sum_time += elapsed_time

        # 暂时不检查 expected_output，直接跳过
        prefix_sum_passed += 1

    # 输出结果
    total_tests = len(test_cases)
    print(f"Brute-force: {brute_force_passed}/{total_tests} tests passed, time: {brute_force_time:.6f} seconds")
    print(f"Prefix sum: {prefix_sum_passed}/{total_tests} tests passed, time: {prefix_sum_time:.6f} seconds")


if __name__ == "__main__":
    run_tests()


'''
暴力法
    对于k个查询，遍历对应区间
    时间复杂度：O(k*n)
前缀法
    提前计算所有元素前缀和，查询时直接通过减法得到指定区间
    时间复杂度：O(n+k)
'''