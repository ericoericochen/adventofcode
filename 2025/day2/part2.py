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


def is_invalid_id(id: int):
    id = str(id)
    num_digits = len(id)

    for i in range(1, num_digits // 2 + 1):
        if num_digits % i != 0:
            continue

        r = id[:i]
        n = num_digits // i
        if r * n == id:
            return True

    return False


def sum_of_invalid_ids(rs: list[tuple[int, int]]) -> int:
    result = 0
    for r in rs:
        start, end = r
        for n in range(start, end + 1):
            if is_invalid_id(n):
                result += n
    return result


id_ranges = read_id_ranges(input_file)
result = sum_of_invalid_ids(id_ranges)
print("result: ", result)
