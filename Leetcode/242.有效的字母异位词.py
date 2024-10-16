#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#


# @lc code=start
class Solution:
    # 方法一：排序
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # 方法二：哈希表, 类型：数组，只适用于小写字母
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26  # 创建一个长度为26的数组，每个位置代表一个字母的计数
        for i in range(len(s)):
            # ord()函数返回字符的ASCII码
            counter[ord(s[i]) - ord("a")] += 1  # 增加字符对应位置的计数
            counter[ord(t[i]) - ord("a")] -= 1  # 减少字符对应位置的计数
        for count in counter:
            if count != 0:  # 如果有任何位置不是0，说明字符数不匹配
                return False
        return True

    # 方法三：哈希表，类型：字典，适用于所有字符
    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for i in range(len(s)):
            counter[s[i]] = (
                counter.get(s[i], 0) + 1
            )  # counter.get(s[i], 0)表示获取s[i]的值，如果不存在则返回0
            counter[t[i]] = counter.get(t[i], 0) - 1
        for count in counter.values():
            if count != 0:
                return False
        return True

    # 方法四：哈希表，类型：defaultdict，适用于所有字符
    def isAnagram4(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = collections.defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1
        for count in counter.values():
            if count != 0:
                return False
        return True

    # 方法五：哈希表，类型：Counter，适用于所有字符
    def isAnagram5(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
        # Counter(s)=Counter({'a': 2, 'b': 1, 'c': 1}), Counter(t)=Counter({'a': 2, 'b': 1, 'c': 1})

    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagram1(s, t)


# @lc code=end
