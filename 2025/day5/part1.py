input_file = "./inputs/day5.txt"

ranges = []
ids = []
with open(input_file) as f:
    is_range = True
    for line in f:
        if line == "\n":
            is_range = False
            continue

        line = line.strip()
        if is_range:
            start, end = line.split("-")
            start, end = int(start), int(end)
            ranges.append((start, end))
        else:
            ids.append(int(line))

fresh = 0
for id in ids:
    for r in ranges:
        if r[0] <= id <= r[1]:
            fresh += 1
            break

print("fresh: ", fresh)
