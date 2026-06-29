# 最优解法：三次反转法（空间 O (1)） —— 全部反转 → 反转前 k 个 → 反转后面剩下的
# [1,2,3,4,5,6,7]，k=3 ——> [7,6,5,4,3,2,1] ——> [5,6,7,4,3,2,1] ——> [5,6,7,1,2,3,4]

from typing import List

# 直接对原数组进行操作，不需要最终返回什么结果
def invertK(nums: List[int], k: int) -> None:
    # 首先一个问题就是，k 为向右移动步数，可能大于数组长度，这个时候取模
    n = len(nums)
    if k > n:
        k = k % n

    # 定义翻转函数 —— left 和 right 对应的是左右索引
    def reverse(left, right):
        # 根据上面的例子就可以看出，翻转就是左右节点对应的位置交换
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # 执行三次翻转
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)


nums1 = [1,2,3,4,5,6,7]
k1 = 3
invertK(nums1,k1)           # 这是一步执行操作
print(nums1)

nums2 = [-1,-100,3,99]
k2 = 2
invertK(nums2,k2)
print(nums2)