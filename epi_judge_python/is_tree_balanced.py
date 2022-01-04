from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple

nodeStats = namedtuple('nodeStats', 'balanced height')

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def testBalance(node: BinaryTreeNode) -> nodeStats:
        if not node:
            return nodeStats(True, 0)
        elif not node.left and not node.right:
            return nodeStats(True, 1)
        else:
            leftStats = testBalance(node.left)
            if not leftStats.balanced:
                return leftStats

            rightStats = testBalance(node.right)
            if not rightStats.balanced:
                return rightStats

            subTreeBalanced = leftStats.balanced and rightStats.balanced and abs(leftStats.height - rightStats.height) <= 1
            subTreeHeight = 1 + max(leftStats.height, rightStats.height)

            return nodeStats(subTreeBalanced, subTreeHeight)

    return testBalance(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
