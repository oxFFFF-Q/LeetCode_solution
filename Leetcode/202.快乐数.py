#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#


# @lc code=start
class Solution:
    # 方法一：哈希表, 类型：集合
    def isHappy1(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1

    # 方法二：快慢指针
    def isHappy2(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

    # 方法三：数学
    def isHappy3(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
        while n != 1 and n not in cycle_members:
            n = get_next(n)
        return n == 1

    # 方法四：数学
    def isHappy4(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

    def isHappy(self, n: int) -> bool:
        return self.isHappy1(n)


# @lc code=end


# 总结
# 1. 方法一使用了哈希表的方法，判断是否出现循环
# 2. 方法二使用了快慢指针的方法，判断是否出现循环

# 时间复杂度分析：
# 方法一/二/三/四的时间复杂度为O(logn)，其中n是输入的数字