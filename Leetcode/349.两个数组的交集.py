#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#


# @lc code=start
class Solution:
    # 方法一：哈希表, 类型：数组
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    # 方法二：哈希表, 类型：集合
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(
            set(nums1).intersection(set(nums2))
        )  # intersection()返回两个集合的交集

    # 方法三：哈希表, 类型：Counter
    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(
            (collections.Counter(nums1) & collections.Counter(nums2)).elements()
        )  # elements()返回交集的元素
        # Counter(nums1)=Counter({1: 2, 2: 2, 3: 1}), Counter(nums2)=Counter({2: 2, 3: 2, 4: 1})
        # Counter(nums1) & Counter(nums2)=Counter({2: 2, 3: 1}), elements()=2, 2, 3

    # 方法四：排序+双指针
    def intersection4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

    # 方法五：排序+二分查找
    def intersection5(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        nums1.sort()
        res = []
        for num in set(nums2):
            if binary_search(nums1, num):
                res.append(num)
        return res

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.intersection1(nums1, nums2)


# @lc code=end

# 总结
# 1. 方法一和方法二都是使用了集合的交集操作，返回两个数组的交集
# 2. 方法三使用了Counter的交集操作，返回两个数组的交集
# 3. 方法四使用了排序+双指针的方法，返回两个数组的交集
# 4. 方法五使用了排序+二分查找的方法，返回两个数组的交集

# 时间复杂度分析：
# 方法一/二/三的时间复杂度为O(n+m)，其中n和m分别是nums1和nums2的长度
# 方法四/五的时间复杂度为O(nlogn+mlogm)，其中n和m分别是nums1和nums2的长度
