input_file = "./inputs/day2.txt"


def read_id_ranges(f: str) -> list[tuple[int, int]]:
    id_ranges = []
    with open(f, "r") as f:
        s = f.read()
    ranges = s.split(",")
    for r in ranges:
        start, end = r.split("-")
        start, end = int(start), int(end)
        id_ranges.append((start, end))
    return id_ranges


def sum_of_invalid_ids(rs: list[tuple[int, int]]) -> int:
    result = 0
    for r in rs:
        start, end = r
        for n in range(start, end + 1):
            n = str(n)
            if len(n) % 2 == 1:
                continue
            h = len(n) // 2
            if n[:h] == n[h:]:
                result += int(n)
    return result


id_ranges = read_id_ranges(input_file)
result = sum_of_invalid_ids(id_ranges)
print("result: ", result)
