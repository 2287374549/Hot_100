# 时间复杂度为 O(n) 并且只使用常数级别额外空间 O(1)
from typing import List

def getMinPos(nums: List[int]) -> int:
    # 一个长为 n 的数组
    # 如果所有的元素都为正整数，从 1 到 n 的话，最小 Pos 为 n+1
    # 如果有元素不在 [1,n] 范围内，则这个未出现的 MinPos 就必然为 [1,n] 中未出现的第一个（遍历）

    # 思路: 正整数从 1 开始, 1 放索引 0 的位置，也就是——数值为 i+1 的数对应的索引为 i
    # 再遍历，第一个不是 nums[i] == i+1 的，对应的 i+1，就是缺失的这个数
    # 又因为空间为 O(1)，所以不声明别的空间数组，直接对原数组进行操作

    n = len(nums)
    for i in range(n):      # i 是索引，使索引为 i 对应的数组中的位置的数值为 i+1
        # 有个点就是，我既然要找到满足 nums[i] != i+1，就是要找到 nums[i] 这个数值正确应该放的位置
        # 所以有个判断就是 nums[nums[i]-1] != nums[i] —— 本质就是遍历 nums[i]，然后将其放到正确的位置上
        while 1 <= nums[i] <= n and nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
            # 需要注意的其实就是这个其实是 while，就是只要这三个条件都满足就一直交换
            # 因为也不能直接丢掉 nums[nums[i]-1] 这个位置原本的数，所以这里其实是交换
            target_idx = nums[i]-1              # 这个是必须的，不然直接 nums[i]-1 用在下面的话，nums[i] 是会变的
            nums[i], nums[target_idx] = nums[target_idx], nums[i]

    # 上面已经交换完了，就可以开始遍历了
    for i in range(n):
        if nums[i] != i+1:
            return i+1

    # 当 1~n 都存在
    return n+1


nums1 = [1,2,0]
print(getMinPos(nums1))
nums2 = [3,4,-1,1]
print(getMinPos(nums2))
nums3 = [7,8,9,11,12]
print(getMinPos(nums3))