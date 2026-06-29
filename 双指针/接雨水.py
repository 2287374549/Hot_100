from typing import List

class Solution:
    # 方案一：前缀最大高度值的数组和后缀最大高度值的数组 —— 时间和空间都是 O(n)
    def trap1(self, height: List[int]) -> int:
        # 额外两个数组 —— 存从左到右最大高度和从右到左的最大高度
        # height[i]，可以视为一个底部长度为 1 的桶
        # 每个桶存的雨水数目，由其左右两边最大高度和自身高度决定
        n = len(height)
        max_left = [0] * n              # 注意记住这个表达，不用加什么 List 和 int
        max_right = [0] * n             # 直接就是 [0] 了

        # 先遍历左边
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        # 再遍历右边 —— 从右往左遍历的
        # 左闭右开，[n-2,-1) -> [n-2,0]，因为 n-1+1=n 超出索引
        max_right[n-1] = height[n-1]                # 这句也可以写成 m_r[-1] = h[-1] —— 最后一个
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        # 最后开始计算最大的接雨水数 —— 所有桶数之和（决定接雨水高度的不是 max，是 min）
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]

        return res

    # 方案二：空间上进行优化
    def trap2(self, height:List[int]) -> int:
        # 左边的和右边的前缀最大值，如果都算了一部分的话（中间不知道）
        # 如果左边比已知的右边要小的话，则当前桶直接 left[i]-height[i] —— 右边同理
        # 空间优化：不用两个数组，用指针来进行操作，指针只移动 n 步，时间 O(n)，没用数组，则空间为 O(1)
        n = len(height)
        left = 0
        right = n - 1

        # 存前后的最大值，但是不用数组了
        max_left = 0
        max_right = 0

        res = 0
        # 左右指针常用 while —— 但是这个地方是否取等可以思考一下
        # 循环内部常常设计 left 和 right 的各自的移动
        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            # 下面这个不能直接用一个 min，因为是哪边的更小，就先处理哪边的
            # 所以下面的两个的 height 对应的，一个是 left 一个是 right
            # 比如右边更小，不能先加左边这个 height[left]，因为右边可能有比当前算到的 max_right 更大，比 max_left 更小的
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1

        return res


solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
res1 = solution.trap1(height)
print(res1)
res2 = solution.trap2(height)
print(res2)