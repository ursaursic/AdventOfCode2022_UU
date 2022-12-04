INPUT = "puzzleInputs/day4.txt"


def check_subset(line: str) -> bool:
    elf_limits = line[:-1].replace('-', ',').split(',')
    elf1 = set([i for i in range(int(elf_limits[0]), int(elf_limits[1])+1)])
    elf2 = set([i for i in range(int(elf_limits[2]), int(elf_limits[3])+1)])
    return (elf1.issubset(elf2) or elf2.issubset(elf1))


def check_intersection(line: str) -> bool:
    elf_limits = line[:-1].replace('-', ',').split(',')
    elf1 = set([i for i in range(int(elf_limits[0]), int(elf_limits[1])+1)])
    elf2 = set([i for i in range(int(elf_limits[2]), int(elf_limits[3])+1)])
    return len(elf2.intersection(elf1)) != 0


def main():
    with open(INPUT, 'r') as f:
        print("Task 1: how many tasks fully contain the other")
        print(sum(check_subset(line) for line in f))
        
    with open(INPUT, 'r') as f:
        print("Task 2: how many tasks overlap")
        print(sum(check_intersection(line) for line in f))


if __name__ == "__main__":
    main()