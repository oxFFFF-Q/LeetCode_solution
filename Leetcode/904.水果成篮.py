#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#


# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        # 计数器，格式为{水果种类: 数量}
        counter = collections.Counter()
        res = 0
        # 右指针右移，左指针不动，直到满足条件
        for right in range(len(fruits)):
            # 右指针右移，更新计数器
            counter[fruits[right]] += 1
            # 通过计数器的长度判断是否满足条件
            while len(counter) > 2:
                # 左指针右移，更新计数器
                counter[fruits[left]] -= 1
                # 如果计数器中的水果数量为0，删除该水果
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1
            # 比较当前子数组长度和之前的最大长度并更新
            res = max(res, right - left + 1)
        return res


# @lc code=end

# 总结：滑动窗口
# 与209相比，判断条件不同
# 关于计数器 collections.Counter()，属于字典的一种，格式为{key: value}
# 不同于一般dict，对于不存在的键，counter[key] 默认为0，所以可以直接使用counter[key] += 1
# 本题判断条件需要统计窗口中不同水果的数量，使用计数器可以方便地实现

# 复杂度分析
# 时间复杂度：O(n)，其中 n 是数组的长度。指针 left 和 right 最多各移动 n 次。
