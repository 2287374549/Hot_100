class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0    # 慢指针直接初始化为 0，一直指着最后确定不为 0 的那个数的下一个

        # 快指针从 0 开始进行遍历数组中的所有的数字（slow 和 fast 都是从 0 开始的）
        for fast in range((len(nums))):
            if(nums[fast] != 0):            # 快指针这个数不为 0，就放到慢指针处
                # save = nums[slow]
                # nums[slow] = nums[fast]
                # nums[fast] = save

                # 这个可以同时交换的感觉 ———— 交换的是数值，这一步并不代码指针移动了
                nums[slow], nums[fast] = nums[fast], nums[slow]

                slow += 1                   # 只有 fast 对应的不为 0 的时候，slow 才往后移

def main():
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    solution.moveZeroes(nums)

    # 上述函数没有返回值，直接对原本的 nums 进行的操作
    # 所以直接调用原函数后，打印这个 nums 就可以
    print(nums)


# 程序入口
if __name__ == "__main__":
    main()

