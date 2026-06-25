class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 特殊情况，如果 t 比 s 长，不可能有覆盖子串
        if len(s) < len(t):
            return ""

        # 先查看 t 中各个字符各自有多少个，哈希，键值对 t_need[char]=count
        t_need = {}
        for c in t:
            t_need[c] = t_need.get(c, 0) + 1

        # 需要满足的 char 的种类 —— 键的数量
        t_count = len(t_need)
        # 当前满足的种类的数量
        count = 0

        # --------------------------------------- 思路 ---------------------------------------
        # 双指针，移动窗口，右边遍历，满足条件（count = t_count）就开始收缩左边，找到 min_len
        left = 0
        right = 0                           # 从左到右遍历，所以都从 0 开始
        win_need = {}                       # 对应 t_need 的存在

        # 因为最终返回的是数组形式，不仅要知道 min_len，还需要知道这个最小长度对应的起点的位置，也就是 left
        min_len = float("inf")              # 无穷大
        min_start = -1                      # 便于取 “” 的返回值

        #
        while right < len(s):               # 记得要更新 right 呀
            char = s[right]
            if char in t_need:
                win_need[char] = win_need.get(char, 0) + 1
                # 放在上一个 if 中，只有加了再判断，当某个 key 满足了，就对 count+1
                if win_need[char] == t_need[char]:
                    # 只有等于的时候才加,实际上,可能出现 win>t 的时候，不会加第二次
                    # 就是因为有这种 “>” 的情况，所有可以通过移出左边来找最小，
                    count += 1

            # 当所有都开始满足的时候，就可以移出左边界 —— 多次移动，用 while
            while left <= right and count == t_count:
                # 能进入这个 while，说明此时的 left 是满足条件的 left
                # 先更新 min_len 和 min_start，再移动 left，因为移动后不一定满足 count == t_count 了
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    min_start = left        # 只有 cur_len 小的时候才更新这个 min_start

                # 开始移动与判断 —— 包含对 count 进行更新，这样才能跳出这个 while
                l_char = s[left]
                if l_char in win_need:
                    win_need[l_char] -= 1  # 移出左指针
                    # 窗口中这个 char 如果数目大于 t_need 的，则依旧是满足条件的，就不用更新 count
                    if win_need[l_char] < t_need[l_char]:
                        count -= 1
                left += 1                           # 先移出当前的，再对 left+1，因为 left 从 0 开始

            right += 1

        if min_start == -1:         # 说明没有进入 while count == t_count，没有满足条件的
            return ""
        return s[min_start:min_start + min_len]


solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))