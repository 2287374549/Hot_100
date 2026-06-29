class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 左右指针
        # 容量受限于X长度和低的指针吗，因此，移动高的指针结果一定变小，移动低的则可能容量变大

        left = 0
        right = len(height) - 1     # 相当于是索引，所以这里要求用 -1

        max_V = 0

        while left < right:
            current_V = min(height[left], height[right]) * (right - left)
            max_V = max(max_V, current_V)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_V

def main():
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    max_V = solution.maxArea(nums)

    # 上述函数没有返回值，直接对原本的 nums 进行的操作
    # 所以直接调用原函数后，打印这个 nums 就可以
    print(max_V)


# 程序入口
if __name__ == "__main__":
    main()
