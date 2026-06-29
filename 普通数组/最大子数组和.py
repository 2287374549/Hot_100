from typing import List

# # 类 —— 有 self，下面声明类的时候记得加上括号
# class Solution:
# # 定义了 nums 是数组形式，而返回的值是 int 形式
#     def maxSubArray(self, nums: List[int]) -> int:
#         # 先声明空间 —— 都是先直接把第一个参数放入
#         current_max = nums[0]
#         res_max = nums[0]
#
#         # 上述已经定义了第一个数了，这里直接从第二个数也就是索引为 2 的时候开始
#         for i in range(1, len(nums)):
#             # 逻辑上，如果 current_num < 0, 则会拖累当前的 nums[i]，直接舍弃之前的结果
#             # 相当于另起灶炉，下面直接用 max，就是运用了 current_num < 0 这个点
#             current_max = max(nums[i], nums[i]+current_max)
#
#             # 每次要记得更新一下
#             res_max = max(current_max, res_max)
#
#         return res_max
#
#
# def main():
#     nums = [-2,1,-3,4,-1,2,1,-5,4]
#     solution = Solution()
#     res = solution.maxSubArray(nums)
#     print(res)
#
# if __name__ == "__main__":
#     main()


# 书写方案二，直接是函数和对函数的运用，不用再写主函数部分了
# 外部没有类的属性，因此这里 def 函数的时候不要加 self
def maxSubArray(nums: List[int]) -> int:
    # 先声明空间 —— 都是先直接把第一个参数放入
    current_max = nums[0]
    res_max = nums[0]

    # 上述已经定义了第一个数了，这里直接从第二个数也就是索引为 2 的时候开始
    for i in range(1, len(nums)):
        # 逻辑上，如果 current_num < 0, 则会拖累当前的 nums[i]，直接舍弃之前的结果
        # 相当于另起灶炉，下面直接用 max，就是运用了 current_num < 0 这个点
        current_max = max(nums[i], nums[i]+current_max)

        # 每次要记得更新一下
        res_max = max(current_max, res_max)

    return res_max

nums = [-2,1,-3,4,-1,2,1,-5,4]
res = maxSubArray(nums)
print(res)
