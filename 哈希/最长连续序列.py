# 时间复杂度必须 O(n)（不能排序，排序是 O (n log n)） —— n 个数都只能调用一次
# 只在序列开头才往后查，不重复遍历，保证 O (n) —— 起点判断：x-1 不在集合里（说明 x 是一段连续数字的开头）

from typing import List

def maxSub(nums: List[int]) -> int:
    max_len = 0        # 最终返回的变量

    # # 写法一：Hash Map
    # map = {}              # 哈希
    # for num in nums:      # 如果存索引的话，for i,num in enumerate(nums)
    #     map[num] = 1      # 这一步不需要存索引 —— 只需要标出这个数存在

    # 写法二：直接用 set，将数组转为集合
    num_set = set(nums)
    map = num_set           # 这一步是为了不改下面的代码所以加上的，实际下面的 map 可以换成 num_set

    for num in map:
        # 如果 num-1 不存在，说明 num 可以为一个子序列的起点
        if (num-1) not in map:
            # 开始以 num 为起点算，因此先定义一个 cnt=1, 后面每多一个数字则 +1
            cnt = 1
            cur = num     # 这个记录是因为以 num 为起点，不能直接变 num（其实另外定义一个 i 来循环也可以，差不多一个意思吧）、
            while (cur+1) in map:
                cnt += 1
                cur += 1
            # 只有当有新的起点出现，才说明需要更新一下当前的 max_len，因此在 for 内部， while 外部
            max_len = max(max_len, cnt)

    return max_len


nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
print(maxSub(nums1))
print(maxSub(nums2))