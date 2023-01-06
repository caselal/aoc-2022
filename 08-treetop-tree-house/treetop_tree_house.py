"""
Advent of Code - Day 8: Treetop Tree House
"""
import numpy as np

with open('input.txt', 'r') as input:
    tree_map = input.read()

tree_map = tree_map.splitlines()

tree_map = [[int(i) for i in list(line)] for line in tree_map]
tree_array = np.asarray(tree_map)

total_trees = np.asarray(tree_map).size

###########
# Part One
###########
hidden_trees_count = 0
surrounding_trees = []

for i, row in enumerate(tree_map[1:-1]):
    for j, tree in enumerate(row[1:-1]):
        # check all tree heights left, right, above, below
        if (max(tree_array[i + 1, :j + 1]) >= tree) and (max(
                tree_array[i + 1, j + 2:]) >= tree) and (max(
                    tree_array[:i + 1, j + 1]) >= tree) and (max(
                        tree_array[i + 2:, j + 1]) >= tree):
            hidden_trees_count += 1

visible_trees_count = total_trees - hidden_trees_count
print(visible_trees_count)

############
# Part Two
############
scenic_score = 0
max_score = 0

for i, row in enumerate(tree_map[1:-1]):
    for j, tree in enumerate(row[1:-1]):
        tree_lines = [
            tree_array[i + 1, :j + 1][::-1], tree_array[i + 1, j + 2:],
            tree_array[:i + 1, j + 1][::-1], tree_array[i + 2:, j + 1]
        ]

        scenic_score = 1

        for tree_line in tree_lines:
            count = 0
            for t in tree_line:
                count += 1
                if t >= tree:
                    break
            scenic_score *= count
        max_score = max(max_score, scenic_score)

print(max_score)
