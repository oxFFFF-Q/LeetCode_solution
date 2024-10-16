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

import sys


def compute_prefix_sums(vec, n):
    p = [0] * n
    p[0] = vec[0]
    for i in range(1, n):
        p[i] = p[i - 1] + vec[i]
    return p


def process_queries(p, queries):
    results = []
    for a, b in queries:
        if a == 0:
            results.append(p[b])
        else:
            results.append(p[b] - p[a - 1])
    return results


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    vec = data[1 : n + 1]
    queries = [(data[i], data[i + 1]) for i in range(n + 1, len(data), 2)]

    prefix_sums = compute_prefix_sums(vec, n)
    results = process_queries(prefix_sums, queries)

    sys.stdout.write("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    main()


# 测试用例
def run_tests():
    import io
    import sys

    test_cases = [
        ("5\n1\n2\n3\n4\n5\n0 1\n1 3\n", "3\n9\n"),
        ("3\n10\n20\n30\n0 0\n1 2\n0 2\n", "10\n50\n60\n"),
        ("4\n1\n2\n3\n4\n0 3\n2 3\n1 2\n", "10\n7\n5\n"),
    ]

    for i, (input_data, expected_output) in enumerate(test_cases):
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()

        main()

        output = sys.stdout.getvalue()
        assert (
            output == expected_output
        ), f"Test case {i+1} failed: Expected {expected_output}, but got {output}"

        print(f"Test case {i+1} passed.")


if __name__ == "__main__":
    run_tests()


# 总结：
# 通过提前计算前缀和，可以简化计算区间和的过程，例如计算区间 [a, b] 的和，只需要计算 p[b] - p[a-1] 即可

# 复杂度分析：
# 时间复杂度：O(n)，n是数组的长度
