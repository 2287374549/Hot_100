class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 一个空房间：map[key] = value，此处位 map[特征词] = ['单词1', '单词2']
        map = {}

        # 开始遍历所有的字符并得到特征词
        for s in strs:
            # sorted：把字符串按字母顺序排序，比如 "eat" 会变成 ['a', 'e', 't']
            # "".join(['a', 'e', 't']) 就会变成重新组合好的字符串 "aet"
            feature_key = "".join(sorted(s))

            # 这个 if 判断可以省略，如果没有，使用下面的那句 append 的会直接自动创建空的列表
            if feature_key not in map:      # 当前还没有这样的 key 的话，先初始化一个空的列表才能往里面放东西
                map[feature_key] = []

            map[feature_key].append(s)      # 这里不是用赋值的方式，用 append 是因为对应的是列表

        # 遍历完就是直接得到分好组之后的结果了
        return list(map.values())           # values 就是直接获取所有的列表（这样不会输出 key）


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    the_list = solution.groupAnagrams(strs)
    print(the_list)


if __name__ == "__main__":
    main()