class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0

        # 0 表示起始点，意思是前缀和为 0 的情况出现了 1 次
        map = {0 : 1}

        sum = 0
        # 遍历 nums 中的所有的数字，注意这里不是 range 这种范围
        for num in nums:
            sum += num
            leave = sum - k         # 我要查看是否有数值和为 k，即查看是否有数值和为 sum - k（因为说了是整数，但是可能有负数）

            if leave in map:
                # 不是加 1，就是 sum - k 出现了多少次，则，剩余的数就可能出现了多少次 k（子数组是连续的，但是可能有负数导致多次出现）
                count += map[leave]

            # 这个 get 意思是，如果有 sum 则得到 map[sum] 即 sum 对应的出现次数，没有则为 0 次
            # 在现有的次数的基础上 + 1
            map[sum] = map.get(sum, 0) + 1

        return count

def main():
    # nums = [1,1,1]
    # k = 2
    nums = [1, 2, 3]
    k = 3
    solution = Solution()
    count = solution.subarraySum(nums, k)

    # 上述函数没有返回值，直接对原本的 nums 进行的操作
    # 所以直接调用原函数后，打印这个 nums 就可以
    print(count)


# 程序入口
if __name__ == "__main__":
    main()