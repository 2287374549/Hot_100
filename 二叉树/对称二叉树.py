from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 没有括号，这个类下是两个函数调用，不是 TreeNode 的 __init__
# 函数内部互相调用 (或者自己调用自己，用 self)
class Solution:
    """
    力扣101题：对称二叉树

    题目描述：
    给定一个二叉树，检查它是否是镜像对称的。
    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    但是 [1,2,2,null,3,null,3] 不是镜像对称的。

    解题思路：
    递归法：如果一个树的左子树和右子树是镜像对称的，则该树是对称的。
    对于两棵树L和R，判断它们是否镜像对称的条件：
    1. L和R的根节点值相同
    2. L的左子树与R的右子树镜像对称
    3. L的右子树与R的左子树镜像对称
    """
    def isTheTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:            # 先考虑这个，也算递归的归
            return True

        # 如果一个树对称，则其左右子树镜像
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1:Optional[TreeNode], root2:Optional[TreeNode]) -> bool:
        # 下方的两个 None 的 if，其实也是递归的归
        if root1 is None and root2 is None:
            return True
        # 只有一棵树为空，镜像不对称 ———— 这个 or 是包含两者都为 None 的时候的
        # 但是上方 and 已经判断了那个情况了，因此到这步的时候，已经不会出现两者都为 None 了
        if root1 is None or root2 is None:
            return False

        # 镜像判断的话：左右节点数值相同 且 左的左子树镜像对称于右的右子树 且 左的右镜像对称于右的左
        # 只有 val 用 ==，其他是判断
        return (root1.val == root2.val and
                self.isMirror(root1.left, root2.right) and
                self.isMirror(root1.right, root2.left))

if __name__ == "__main__":
    # 构建测试用例 [1,2,2,3,4,4,3]
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))      # root1.left.left = TreeNode(3)
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))

    # 构建测试用例 [1,2,2,null,3,null,3]
    #       1
    #      / \
    #     2   2
    #      \   \
    #       3   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2, right=TreeNode(3))
    root2.right = TreeNode(2, right=TreeNode(3))

    solution = Solution()

    print(f"测试用例1 [1,2,2,3,4,4,3] 是否对称: {solution.isTheTree(root1)}")  # True
    print(f"测试用例2 [1,2,2,null,3,null,3] 是否对称: {solution.isTheTree(root2)}")  # False