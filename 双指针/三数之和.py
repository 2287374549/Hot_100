# 先给数组排序（方便双指针 + 方便去重）
# 固定一个数 nums [i] —— 用左右双指针找另外两个数
# 左指针：i+1（前面的找过了，前面的要么是包含其能找到三个数满足条件，要么是不能满足条件）； 右指针：len(nums)-1

from typing import List

def ThreeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()              # 首先要排序，使得数组内部数字是由小到大的
    res = []                 # 定义最终返回结果
    n = len(nums)            # 是 len，便于下方依次遍历排序后的所有的数

    for i in range(n):
        if nums[i] > 0:      # 从小到大，如果第一个数就大于 0 了，则加上两个数就不可能为 0 了
            break            # 直接跳出这一整个 for 循环，后面的都不用继续循环了，好像感觉这里直接 return res 也行？？？

        # 去重：第一个数重复，跳过 !!!!!!!!!!!!!!!!!! 如果当前数和前一个一样，比如 [-1,-1, ...]，会产生重复三元组，直接跳过。
        # i 之所以要大于 0，是因为要有 i-1 的存在
        # 如果新的这个和上一个一样的话，那么这个最终所取的值也会和上一个一样（或者这个直接无法满足条件，比如[-1,-1,2,3]，必须两个 -1 才行）
        if i > 0 and nums[i] == nums[i-1]:
            continue         # 这是跳出这一次的 i，而不是不进行后续的操作了


        left = i+1
        right = n-1          # 左右指针对应的是索引

        while left < right:  # 双指针一左一右很多都是这个判断条件
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])          # 注意中括号，返回的是 List[List[int]]

                # 还需要避免的一点就是，如果有多个需要处理的呢？最终返回的是数字，不是索引，所以如果有数字重复的，应该只存取一次
                # 下面之所以那样写，也是因为我已经按照顺序排序了，相同的值对应的索引都是挨着的
                while left < right and nums[left] == nums[left+1]:      # 先左指针把所有重复的走完，是先认为当前和下一个重复了，把指针移动到下一个的位置
                    left += 1
                while left < right and nums[right] == nums[right-1]:    # 再把右边重复的走完
                    right -= 1

                # 上面是如果重复则更新 left 和 right —— 走完上面后是左右指针都对应的是重复的最后一个，也就是已经加入 res 中的数值，所以还得再挪动才是开始计算下一组
                left += 1
                right -= 1

            elif total < 0:
                left += 1                                               # 越在右边数字越大
            else:
                right -= 1

    return res


nums1 = [-1,0,1,2,-1,-4]
print(ThreeSum(nums1))
nums2 = [0,1,1]
print(ThreeSum(nums2))
nums3 = [0,0,0]
print(ThreeSum(nums3))
