class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 哈希，用来存 left 对应的字符和位置， map[char] = index
        char_dict = {}

        left = 0
        max_len = 0

        # 用 right 来遍历整个数组，看当前 right 是否对应已重复的那个字符
        # 只要框里没有重复的字符，则计算当前的长度
        for right in range(len(s)):
            char = s[right]
            # 【核心逻辑】如果字符之前出现过，并且它还在我们当前的窗口内！
            if char in char_dict and char_dict[char] >= left:
                # 只有当 left 对应的是重复的这个字符的下一个，才说明当前 left 到 right 中没有重复的
                # 因为是”子串“，所以需要满足必须是连着的，如果之前这个字符出现过，就只能定位到重复的这个的下一个才行了
                left = char_dict[char] + 1

            char_dict[char] = right         # 不管是不是重复的，都需要将当前这个保存下来

            current_len = right - left + 1
            max_len = max(max_len, current_len)

        return max_len

def main():
    s = "abcabcbb"
    solution = Solution()
    max_len = solution.lengthOfLongestSubstring(s)

    # 上述函数没有返回值，直接对原本的 nums 进行的操作
    # 所以直接调用原函数后，打印这个 nums 就可以
    print(max_len)


# 程序入口
if __name__ == "__main__":
    main()
