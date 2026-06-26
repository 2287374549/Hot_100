"""
力扣 #543 - 二叉树的直径

题目描述：
给定一棵二叉树的根节点 root，返回它的直径长度。
二叉树的直径是任意两个节点之间最长路径的长度，
这条路径可能经过也可能不经过根节点。

解题思路：
对于每个节点，直径 = 左子树高度 + 右子树高度
我们递归计算每个节点的高度，同时更新最大直径。

时间复杂度：O(N)，每个节点只访问一次
空间复杂度：O(H)，H 为树的高度（递归栈深度）
"""

from typing import List, Optional

class TreeNode:
    """二叉树节点定义"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历生成树的函数，最后返回的是树的根节点
def getTree(values: List[int]) -> Optional[TreeNode]:
    # 测试用例 1: [1,2,3,4,5]
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # 直径 = 3 (路径: 4 -> 2 -> 1 -> 3)

    root = TreeNode(values[0])          # 记得加上 TreeNode 呀
    queue = [root]                      # 注意这个的格式

    i = 1                               # 从 1 开始是因为 values[0] 已经是根节点 root 的了

    # values 中还有数值 并且 queue 中还有节点没有处理完
    while i < len(values) and queue:
        # 先弹出当前节点 —— 从左侧弹出 —— 弹出先放的
        # 先放的左节点，也就先处理左节点 —— 层序遍历
        node = queue.pop(0)

        # 先左 —— 不是很清楚这个 i 大小判断加入的原因
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)     # 这时候存起来是为了待会弹出去为其添加左右节点
        i += 1                          # 即使没有进入上面的循环，i 也要 +1，因为可能是 None

        # 再右，这个 i 大小判断可能是上面的左节点使得 i+=1 后超出索引了
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    def getDiaMeter(self, root: Optional[TreeNode]) -> int:
        # 直径是两个节点间最长路径 —— 加 self 下面要用
        self.max_meter = 0

        # 最长路径是左子树深度+右子树深度 —— 得到最大深度的同时更新 max_meter
        # 这个 getdepth 函数是在 getDiaMeter 内部的，所以不需要加 self
        def getdepth(root: Optional[TreeNode]) -> int:
            if root is None:        # 递归的归
                return 0

            # 这里自己调用自己没有用 self 来着
            # 后序遍历：先计算左右子树的高度
            left_depth = getdepth(root.left)
            right_depth = getdepth(root.right)

            self.max_meter = max(left_depth + right_depth, self.max_meter)

            # 当前节点最大深度，左右中的最大加上根节点
            return max(left_depth, right_depth) + 1

        # 上面已经声明好了，这里就可以直接调用了
        getdepth(root)

        # 上述返回值是最大深度，不是我们要的直径，直径直接随着上述调用被更新，这里直接返回即可
        return self.max_meter


if __name__ == "__main__":
    solution = Solution()       # 有括号

    tree1 = [1, 2, 3, 4, 5]
    node1 = getTree(tree1)
    print(solution.getDiaMeter(node1))