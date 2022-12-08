import numpy as np


INPUT = "puzzleInputs/day6.txt"
INPUT_SNR = "puzzleInputs/day6_SNR.txt"


def find_code_marker(code: str) -> int:
    for i in range(len(code)):
        if len(set(code[i:i+4])) == 4:
            return i+4


def find_message_marker(code: str) -> int:
    for i in range(len(code)):
        if len(set(code[i:i+14])) == 14:
            return i+14


def main():
    with open(INPUT, 'r') as f:
        code = f.readline()
        print("Task 1: find the first code marker")
        print(find_code_marker(code))

        print("Task2: find message marker")
        print(find_message_marker(code))
    
    
    # extra tasks
    with open(INPUT_SNR, 'r') as f:
        message_length = 8
        occurances = np.zeros((message_length, 26))
        for line in f:
            for i in range(message_length):
                occurances[i, ord(line[i])-ord('a')] += 1
            
        
        print("Task1 (SNR): max occurances")
        result = ''
        for c in [chr(c + ord('a')) for c in occurances.argmax(axis=1)]:
            result += c
        print(result)

        print("Task2 (SNR): min occurances")
        result = ''
        for c in [chr(c + ord('a')) for c in occurances.argmin(axis=1)]:
            result += c
        print(result)


        
if __name__ == "__main__":
    main()