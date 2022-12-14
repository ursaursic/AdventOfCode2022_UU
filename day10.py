INPUT = "puzzleInputs/day10.txt"


def readout_to_cycles(cycles: list[int], code: str) -> list[int]:
    if code == "noop":
        cycles.append(cycles[-1])
        return cycles
    if code.startswith("addx"):
        cycles.append(cycles[-1])
        cycles.append(cycles[-1] + int(code.split(' ')[1]))
        return cycles


def print_screen(screen: list[bool]) -> None:
    for i in range(len(screen)//40):
        line = ''
        for j in range(i*40, (i+1)*40):
            line += screen[j]
        print(line)


def get_screen_output(cycles: list[int]) -> list[str]:
    screen = list(len(cycles)*[' '])
    for i in range(len(cycles)):
        sprite_pos = [cycles[i] - 1, cycles[i], cycles[i] + 1]
        if i%40 in sprite_pos:
            screen[i] = "#"
    return screen



def main():
    cycles = [1]
    with open(INPUT, 'r') as f:
        for line in f:
            cycles = readout_to_cycles(cycles, line.rstrip())

    print("\nTask1: ")
    cycles_of_interest = [20, 60, 100, 140, 180, 220]
    print(sum([cycles[i-1]*i for i in cycles_of_interest]))

    print("\nTask2: get message on the screen")
    screen = get_screen_output(cycles)
    print_screen(screen)


if __name__ == "__main__":
    main()