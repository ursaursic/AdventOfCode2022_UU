INPUT = "puzzleInputs/day2.txt"


def calc_points_part_1(line: str) -> int:
    if line == 'A X': return 3 + 1
    if line == 'A Y': return 6 + 2
    if line == 'A Z': return 0 + 3

    if line == 'B X': return 0 + 1
    if line == 'B Y': return 3 + 2
    if line == 'B Z': return 6 + 3
    
    if line == 'C X': return 6 + 1
    if line == 'C Y': return 0 + 2
    if line == 'C Z': return 3 + 3


def calc_points_part_2(line: str) -> int:
    if line == 'A X': return 3 + 0
    if line == 'A Y': return 1 + 3
    if line == 'A Z': return 2 + 6

    if line == 'B X': return 1 + 0
    if line == 'B Y': return 2 + 3
    if line == 'B Z': return 3 + 6

    if line == 'C X': return 2 + 0
    if line == 'C Y': return 3 + 3
    if line == 'C Z': return 1 + 6


def main():
    print('Task 1: shit speculation')
    with open(INPUT, "r") as f:
        print(sum(calc_points_part_1(line[:-1]) for line in f))
    
    print('Task 2: actual knowedlege')
    with open(INPUT, "r") as f:
        print(sum(calc_points_part_2(line[:-1]) for line in f))


if __name__ == "__main__":
    main()