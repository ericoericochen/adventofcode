input_file = "./inputs/day3.txt"

N = 12


def read_banks(f: str) -> list[list[int]]:
    banks = []
    with open(f, "r") as f:
        for line in f:
            bank = [int(j) for j in line.strip()]
            banks.append(bank)
    return banks


def get_joltage(bank: list[int], n: int) -> int:
    f = [[0 for j in range(n + 1)] for i in range(len(bank))]

    # f(i, j) - max number that could be formed from x[i:] with j digits
    # initialize f(i, 1)

    for i in range(len(bank)):
        f[i][1] = max(bank[i:])

    for j in range(2, N + 1):
        for i in range(len(bank)):
            if len(bank) - i < j:
                continue

            candidates = []
            for k in range(i, len(bank) - j + 1):
                candidate = int(str(bank[k]) + str(f[k + 1][j - 1]))
                candidates.append(candidate)
            f[i][j] = max(candidates)

    return f[0][N]


def get_total_output_joltage(banks: list[list[int]]) -> int:
    joltage = 0
    for bank in banks:
        joltage += get_joltage(bank, N)
    return joltage


banks = read_banks(input_file)
joltage = get_total_output_joltage(banks)

print("joltage: ", joltage)
