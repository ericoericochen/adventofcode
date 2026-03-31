# input_file = "./inputs/test.txt"
input_file = "./inputs/day9.txt"


def read_corners(fp: str):
    corners = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            corner = tuple([int(n) for n in line.split(",")])
            corners.append(corner)
    return corners


def compute_area(a: tuple[int, int], b: tuple[int, int]) -> int:
    w = abs(a[0] - b[0]) + 1
    h = abs(a[1] - b[1]) + 1
    return w * h


def find_largest_area(corners: list[tuple[int, int]]):
    N = len(corners)
    max_area = -1
    for i in range(N):
        for j in range(i + 1, N):
            a = corners[i]
            b = corners[j]
            area = compute_area(a, b)
            max_area = max(max_area, area)
    return max_area


corners = read_corners(input_file)
area = find_largest_area(corners)
print("area: ", area)
