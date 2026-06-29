from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先按照每个区间的 start 来进行从小到大的排序（保证重叠的都是相邻的）
        # 当满足上述顺序后，如果后者的 start 比前者的 end 小，则重叠，如 [1,3],[2,6]，有 1<2<3 重叠
        # 排序避免了出现 [3,6],[1,2]，依旧是 1<3，但是此处不重叠

        # sort 是内置排序，key 是指定按照什么规则进行排序，x在此处相当于每个小区间 [1,3] 这种，x[0] 指的是区间的 start
        # lambda 是匿名函数的关键字，等价于定义了一个临时的小函数
        intervals.sort(key=lambda x: x[0])

        # 定义返回的类型
        res = []
        for interval in intervals:
            # 当res为空 或者 当res中最后的那个区间的end<interval的start：没有重合直接加
            # res[-1][1] ——> [-1] 指的是最后的一个子区间
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # 出现重合，只需要修改 res 中最后的一个区间的 end 的数值
            else:
                # 比如 [1,10] 和 [2,6] 不能直接取 6，合并应为 [1,10]
                res[-1][1] = max(res[-1][1], interval[1])

        return res

def main():
    solution = Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(solution.merge([[1,4],[4,5]]))                 # [[1,5]]
    print(solution.merge([[4,7],[1,4]]))                 # [[1,7]]

if __name__ == "__main__":
    main()


