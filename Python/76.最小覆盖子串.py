#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        # 格式为{字符: 数量},统计t中字符的数量
        counter = collections.Counter(t)
        # 格式为{字符: 数量},初始化窗口中字符的数量为0
        window = collections.Counter()
        res = float("inf")
        start = 0
        # 记录窗口中满足条件的字符种类数量
        valid = 0
        # 右指针右移，左指针不动，直到满足条件
        for right in range(len(s)):
            # 右指针右移，更新窗口
            if s[right] in counter:
                window[s[right]] += 1
                if window[s[right]] == counter[s[right]]:
                    valid += 1
            # 判断左指针是否需要右移
            while valid == len(counter):
                # 比较当前子串长度和之前的最小长度并更新
                if right - left + 1 < res:
                    res = right - left + 1
                    start = left
                # 左指针右移，更新窗口
                if s[left] in counter:
                    if window[s[left]] == counter[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1
        return "" if res == float("inf") else s[start : start + res]


# @lc code=end

# 总结：滑动窗口
# 与904相比，判断条件不同，需要使用两个计数器，分别统计t中字符的数量和窗口中字符的数量

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是字符串 s 的长度。指针 left 和 right 最多各移动 n 次。
