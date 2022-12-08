INPUT = "puzzleInputs/day8.txt"


import numpy as np


def rotate_view(trees: np.ndarray) -> np.ndarray:
    return np.rot90(trees)


def do_you_see_trees(trees: np.ndarray) -> np.ndarray:
    visible_trees = np.zeros_like(trees, dtype=bool)
    for view in range(4):
        for i in range(trees.shape[0]):
            for j in range(trees.shape[1]): 
                if i == 0 or j == 0:
                    visible_trees[i, j] = True
                    continue
                if trees[i, j] > np.max(trees[i, :j]):
                    visible_trees[i, j] = True
        trees = np.rot90(trees)
        visible_trees = np.rot90(visible_trees)
    return visible_trees


def scenic_scores(trees: np.ndarray) -> np.ndarray:
    scenic_score = np.zeros_like(trees)
    for i in range(1, trees.shape[0]-1):
        for j in range(1, trees.shape[1]-1):
            count_right = 0
            for k in range(1, trees.shape[1]-j):
                count_right += 1
                if trees[i, j+k] >= trees[i, j]:
                    break

            count_left = 0
            for k in range(1, j+1):
                count_left += 1
                if trees[i, j-k] >= trees[i, j]:
                    break

            count_up = 0
            for k in range(1, i+1):
                count_up += 1
                if trees[i-k, j] >= trees[i, j]:
                    break

            count_down = 0
            for k in range(1, trees.shape[0]-i):
                count_down += 1
                if trees[i+k, j] >= trees[i, j]:
                    break

            scenic_score[i, j] = count_left*count_right*count_down*count_up
    return scenic_score


def main():
    with open(INPUT, 'r') as f:
        trees = []
        for line in f:
            list_line = [int(tree) for tree in line.rstrip()]
            trees.append(list_line)
    trees = np.array(trees)
    
    print("Task1: do you see trees?")
    print(np.sum(do_you_see_trees(trees)))
    print("Task2: what's the best spot?")
    print(np.max(scenic_scores(trees)))

        
if __name__ == "__main__":
    main()