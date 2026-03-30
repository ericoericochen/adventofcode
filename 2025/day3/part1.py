input_file = "./inputs/day3.txt"


def read_banks(f: str) -> list[list[int]]:
    banks = []
    with open(f, "r") as f:
        for line in f:
            bank = [int(j) for j in line.strip()]
            banks.append(bank)
    return banks


def get_joltage(bank: list[int]) -> int:
    max_j = -1
    max_index = -1

    for i in range(len(bank) - 1):
        if bank[i] > max_j:
            max_j = bank[i]
            max_index = i

    last_digit = max(bank[max_index + 1 :])
    joltage = int(str(max_j) + str(last_digit))
    return joltage


def get_total_output_joltage(banks: list[list[int]]) -> int:
    joltage = 0
    for bank in banks:
        joltage += get_joltage(bank)
    return joltage


banks = read_banks(input_file)
joltage = get_total_output_joltage(banks)

print("joltage: ", joltage)
