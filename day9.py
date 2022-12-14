from distutils.file_util import move_file

import numpy as np


INPUT = "puzzleInputs/day9.txt"


def force_on_tail(head: np.ndarray, tail: np.ndarray) -> np.ndarray:
    move_tail = [0, 0]
    distance = [abs(head[axis]-tail[axis]) for axis in [0, 1]]
    distance_complex = complex(distance[0], distance[1])
    if abs(distance_complex) == 2:
        move_tail = [(head[axis]-tail[axis])//2 for axis in [0, 1]]
    if abs(distance_complex) > 2:
        move_tail = [(head[axis]-tail[axis])//abs(head[axis]-tail[axis]) for axis in [0, 1]]
    return np.array(move_tail)


def move_head(rule: str) -> np.ndarray:
    if rule == 'R': return np.array([1, 0])
    if rule == 'L': return np.array([-1, 0])
    if rule == 'U': return np.array([0, 1])
    if rule == 'D': return np.array([0, -1])


def move_rope(rope, move_head) -> list[list[int]]:
    rope[0] += move_head
    for i in range(1, len(rope)):
        rope[i] += force_on_tail(rope[i-1], rope[i])
    return rope


def main():
    head = np.array([0, 0])
    tail = np.array([0, 0])
    with open(INPUT, 'r') as f:
        tail_positions = np.zeros((1000, 1000), dtype=bool)
        tail_positions[0, 0] = True
        for rule in f:
            rule = rule.rstrip().split(' ')
            for i in range(int(rule[1])):
                head += move_head(rule[0])
                tail += force_on_tail(head, tail)
                tail_positions[tail[0], tail[1]] = True

    print("Task1: only two knobs")            
    print(np.sum(tail_positions))

    rope = np.array([[0, 0] for i in range(10)])
    with open(INPUT, 'r') as f:
        tail_positions = np.zeros((1000, 1000), dtype=bool)
        tail_positions[0, 0] = True
        for rule in f:
            rule = rule.rstrip().split(' ')
            for i in range(int(rule[1])):
                move_first_knob = move_head(rule[0])
                rope = move_rope(rope, move_first_knob)
                tail_positions[rope[9, 0], rope[9, 1]] = True
    
    print("Task2: long rope")
    print(np.sum(tail_positions))


if __name__ == "__main__":
    main()