input_file = "./inputs/day1.txt"

N = 100
dial = 50
password = 0

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        turns = int(line[1:])

        if direction == "L":
            dial = (dial - turns) % N
        elif direction == "R":
            dial = (dial + turns) % N

        if dial == 0:
            password += 1

print("password: ", password)
