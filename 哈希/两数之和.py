class Solution(object):
    def twoSum(self, nums, target):

        # # Easy
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if target == nums[i] + nums[j]:
        #             return [i,j]
        # return []

        # Difficult
        num_map = {}                                # 存数值和索引（字典——键值对：这里是“数字”对应“索引”）
        for i, num in enumerate(nums):              # enumerate：同时打包元素的“索引(位置)”和“元素的值”
            complement = target - nums[i]
            if complement in num_map:               # 检查 complement 这个变量的值，是否作为键（Key）存在于字典 num_map 中
                return [num_map[complement], i]
            num_map[num] = i                        # num_map[key] = value

        return []

def main():
    # 测试数据
    nums = [2, 7, 11, 15]
    target = 9

    # nums = [3, 2, 4]
    # target = 6

    # nums = [3, 3]
    # target = 6

    # 创建 Solution 实例
    solution = Solution()
    # 调用 twoSum 函数获取结果
    result = solution.twoSum(nums, target)
    # 打印输出
    print("两个数的索引为：", result)


# 程序入口
if __name__ == "__main__":
    main()