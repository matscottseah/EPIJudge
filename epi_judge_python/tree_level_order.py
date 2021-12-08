from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    levels = []
    if not tree:
        return levels

    Q = [tree]
    levelCount = 1

    while len(Q) != 0:
        level = []
        for _ in range(levelCount):
            node = Q[0]
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)

            level.append(node.data)
            Q.pop(0)

        levels.append(level)
        levelCount = len(Q)

    return levels


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
