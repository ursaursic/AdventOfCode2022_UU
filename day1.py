from __future__ import annotations


INPUT = "puzzleInputs/day1.txt"


class Elf:
    def __init__(self) -> None:
        self.snacks = []
        self.total_cal = 0

    
    def __lt__(self, other: Elf) -> bool:
         return self.total_cal < other.total_cal
    

    def add_snack(self, cal: int) -> None:
        self.snacks.append(cal)
        self.total_cal += cal


def main():
    elves = [Elf()]

    elf_counter = 0
    with open(INPUT, "r") as f:
        for line in f:
            if line == '\n':
                elf_counter += 1
                elves.append(Elf())
                continue
            
            elves[elf_counter].add_snack(int(line[:-1]))

    elves.sort()

    print("Max cal: ")
    print(elves[-1].total_cal)
    print("Sum of the first three elves: ")
    print(sum(elf.total_cal for elf in elves[-3:]))


if __name__ == "__main__":
    main()