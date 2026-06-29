class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        # 是在 s 中找 p 的异位词
        if len(s) < len(p):
            return res

        # 用数组的形式统计，a~z 是 26 个小写字母
        # 索引就是 ord('a')=0, ord('z')=25 —— 对应的索引下的数值则是这个字母出现的次数
        p_record = [0]*26
        win_record = [0]*26

        # 先遍历 p 中的字符，i 的取值从 0 到 len(p)-1
        for i in range(len(p)):
            p_record[ord(p[i]) - ord('a')] += 1       # 对应的那个字母的计数上加了一个 1

            # 把 s 的第一个和 p 等长的字符串也进行一个统计
            # 因为找异位词，窗口的长度是固定的，后面移动的时候，是右侧的加进来一个，左侧则去掉一个
            # 所以先计算到后面开始挪动的时候的右侧的那个点的位置
            win_record[ord(s[i]) - ord('a')] += 1

        if p_record == win_record:          # 先判断统计第一个窗口中的情况
            res.append(0)

        for i in range(len(p), len(s)):     # i 的取值范围为 [ len(p), len(s) - 1 ]
            # 在第一个 s 的窗口的基础上，往右挪一个加进来
            win_record[ord(s[i]) - ord('a')] += 1
#           # 因此左侧的那一个得从计数上去掉，就用 i = len(p) 加入，则 i = 0 需要去掉来看， 这里不用多一个 +1
            win_record[ord(s[i - len(p)]) - ord('a')] -= 1

            if p_record == win_record:
                res.append(i - len(p) + 1)  # 依旧是结合上面的这个情况，i=0 去掉，第一个索引就应是 1，因此这里要 +1

        return res


def main():
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    res = solution.findAnagrams(s, p)

    # 上述函数没有返回值，直接对原本的 nums 进行的操作
    # 所以直接调用原函数后，打印这个 nums 就可以
    print(res)


# 程序入口
if __name__ == "__main__":
    main()
