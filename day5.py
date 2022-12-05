INPUT = "puzzleInputs/day5.txt"


class Stack:
    def __init__(self, idx: int) -> None:
        self.stack_idx = idx
        self.crates = []

    def add_crates(self, crates: list[str]) -> None:
        [self.crates.append(crate) for crate in crates]

    def remove_crates(self, n: int) -> list:
        removed_crates = []
        for i in range(n):    
            removed_crates.append(self.crates.pop())
        return removed_crates


def move_crates(task: str, rule: str, crate_system: list[Stack]) -> None:
    rule = rule.rstrip().split(' ')
    move_n = int(rule[1])
    move_from = int(rule[3])-1
    move_to = int(rule[5])-1

    removed_crates = crate_system[move_from].remove_crates(move_n)
    # part1
    if task == "Task1":
        crate_system[move_to].add_crates(removed_crates)
    # part2
    if task == "Task2":
        crate_system[move_to].add_crates(removed_crates[::-1])


def main():
    for task in ["Task1", "Task2"]:
        with open(INPUT, "r") as f:
            data = f.readlines()
            rules = data[10:]
            crate_system = [Stack(int(data[8][j:j+3].strip())) for j in range(0, len(data[8]), 4)]
            for i in range(8):
                crate_line = [data[7-i][j:j+3].strip(' []') for j in range(0, len(data[8]), 4)]
                [crate_system[k].add_crates([crate_line[k]]) for k in range(len(crate_system)) if crate_line[k] != '']

            for rule in rules:
                move_crates(task, rule, crate_system)

            result = ''
            for stack in crate_system:
                result += str(stack.crates[-1])
            print(task + ":")
            print(result)
    
            
if __name__ =="__main__":
    main()