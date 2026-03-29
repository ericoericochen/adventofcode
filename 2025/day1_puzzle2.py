input_file = "./inputs/day1.txt"

N = 100
dial = 50
password = 0


# TODO: this can be simplified
def count_zeros(start: int, end: int, n: int):
    if end < start:
        temp = start
        start = end
        end = temp

    i = start
    if start % n != 0:
        i += n - (start % n)
    j = end - (end % n)

    if not start <= i <= end:
        return 0

    return (j - i) // n + 1


with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        turns = int(line[1:])

        assert turns > 0

        if direction == "L":
            print(line, dial - 1, dial - turns, count_zeros(dial + 1, dial + turns, N))
            password += count_zeros(dial - 1, dial - turns, N)
            dial = (dial - turns) % N
        elif direction == "R":
            print(line, dial - 1, dial - turns, count_zeros(dial + 1, dial + turns, N))
            password += count_zeros(dial + 1, dial + turns, N)
            dial = (dial + turns) % N


print("password: ", password)
