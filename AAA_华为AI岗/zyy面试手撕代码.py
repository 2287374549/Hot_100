# 给定一个正整数数组 values，其中 values[i] 表示第i个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j-i。
# 一对景点 (i<j) 组成的观光组合的得分为 values[i] + values[j] + i - j，也就是景点的评分之和减去它们两者之间的距离。
# 返回 values 中一对观光景点能取得的最高分。
# 输入: values = [8,1,5,2,6]
# 输出:11
# 解释: i=0,j=2, values[i]+ values[j]+i-j=8+5 +0-2=11


values1 = [8, 1, 5, 2, 6]
values2 = [1,2]
values3 = [1,3, 6, 6, 8, 2]
# 方法一，虽然我感觉逻辑可能会有点说不通 —— 豆包说我是错的，这样做可能会遍历不完全
# 比如 values3 —— 可能向左边移动了，但是左边的更小了
def getMaxValue(values:[int]) -> int:
    n = len(values)     # 数组长度
    left = n//2 - 1
    right = n//2
    maxV = values[0] + values[n-1] - (n-1)      # 如果像第二道题那样的话，我直接就进入不了 while 的循环了

    while not (left == 0 and right == n-1):
        maxV = max(maxV, values[left]+values[right]+left-right)

        if (values[left] <= values[right] or right == n-1) and left != 0:
            left -= 1
        elif (values[right] < values[left] or left == 0) and right != n-1:
            right += 1

    return maxV

print(getMaxValue(values1))
print(getMaxValue(values2))
print(getMaxValue(values3))     # 这个就出现了错误
# 而且这个方法吧，要是两个比较大的值都在左边或者都在右边的话，也肯定不对了

print()

# 方法二，固定左指针，遍历右指针的思想呢
def getMaxValue2(values: [int]) -> int:
    # score = (values[i]+i) + (values[j]-j) —— 当 i<j
    max_left = values[0] + 0    # 最大的 values[i]+i
    maxV = 0

    for j in range(1, len(values)):     # 左闭右开 [1, n) 即 [1, n-1]
        maxV = max(maxV, max_left + values[j] - j)
        max_left = max(max_left, values[j] + j)
        # 如果当前的 value[j]+j 大于之前的 max_left，后面的 j 加上当前的 value[j]+j 肯定比当前更大

    return maxV

print(getMaxValue2(values1))
print(getMaxValue2(values2))
print(getMaxValue2(values3))





