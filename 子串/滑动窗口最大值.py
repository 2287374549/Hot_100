class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []

        from collections import deque
        q = deque()     # 双端操作的队列，用来存索引（不是存数值的，只有知道索引才能知道是否在 k 限制的窗口内）
        res = []        # 用来存最终的保存的每个窗口内最大值的数组

        for i in range(len(nums)):                      # i 是索引，取 [0, len(nums)-1]
            # if q 指的是如果 q 不是空的， q[0] 是第一个索引，也是最大的窗口值对应的那个索引
            # 当 i 进入 k 大小的窗口，则，最前面的那个数对应的索引最小为 i-k+1，因为 i-(i-1)=1，但是窗口中两个数
            if q and q[0] < i - k + 1:
                q.popleft()                             # 当前最大的那个数对应的索引如果不在窗口内，则从 q 中左侧踢出去（因为我们设置左边大右边小），再后续判断

            # 接下里的操作是为了保证 q 中索引对应的元素是从小到大排列的（注意这个 while 是在 for 的内部的第二层循环）
            # 相当于就一直循环 q 中的索引，只要不比“新来的”数值大就踢掉，这里是一直在踢，并没有加入的操作
            while q and nums[q[-1]] <= nums[i]:         # q[-1] 指的是最右侧的元素（也就是 q 中索引对应数最小的那个的索引）
                # 如果我“老员工”数值不比“新员工”大，就一直踢
                q.pop()                                 # 这是踢掉最右边那个最小的
            # 把不比 i 对应的数大的数都去掉后，再把这个索引加入进去
            q.append(i)

            # 接下来就是得到 res 结果数值，只有从第一个 k 窗口完整开始才有数值的（即 i 从 0 到 k-1）
            if i >= k-1:
                res.append(nums[q[0]])

        return res

def main():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    res = solution.maxSlidingWindow(nums, k)

    print(res)


# 程序入口
if __name__ == "__main__":
    main()