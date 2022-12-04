INPUT = "puzzleInputs/day3.txt"


def compare_compartments(comp_a: str, comp_b: str) -> int:
    for i in range(len(comp_a)):
        for j in range(len(comp_b)):
            if comp_a[i] == comp_b[j]:
                if ord(comp_a[i]) >= ord('a'):
                    return ord(comp_a[i]) - ord('a') + 1
                return ord(comp_a[i]) - ord('A') + 27


def find_common_item(elf_group: list) -> int:
    for i in range(len(elf_group[0])):
        for j in range(len(elf_group[1])):
            if elf_group[0][i] == elf_group[1][j]:
                for k in range(len(elf_group[2])):
                    if elf_group[0][i] == elf_group[2][k]:
                        if ord(elf_group[0][i]) >= ord('a'):
                            return ord(elf_group[0][i]) - ord('a') + 1
                        return ord(elf_group[0][i]) - ord('A') + 27


def divide_elves(f: list) -> list:
    elf_groups = [[]]
    elf_counter = 0
    for elf in f.readlines():
        if elf_counter == 3:
            elf_groups.append([])
            elf_counter = 0
        elf_groups[-1].append(elf[:-1])
        elf_counter += 1
    return elf_groups


def main():
    with open(INPUT, 'r') as f:
        print("Task 1: sum of priorities")
        print(sum(compare_compartments(line[:len(line)//2], line[len(line)//2:-1]) for line in f))
    with open(INPUT, 'r') as f:
        elf_groups = divide_elves(f)
        print('Task2: get elf groups')
        print(sum(find_common_item(elf_group) for elf_group in elf_groups))


if __name__ == "__main__":
    main()