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
sorted_ranges = sorted(ranges)


# a is the first range, b is the second range, b[0] >= a[0]
def combine_range(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0], max(a[1], b[1]))


combined_ranges = [sorted_ranges[0]]
for i in range(1, len(sorted_ranges)):
    prev_r = combined_ranges[-1]
    r = sorted_ranges[i]

    if r[0] <= prev_r[1]:
        combined_ranges[-1] = combine_range(prev_r, r)
    else:
        combined_ranges.append(r)


fresh = 0
for r in combined_ranges:
    fresh += r[1] - r[0] + 1

print("fresh: ", fresh)
