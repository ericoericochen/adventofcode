input_file = "./inputs/day4.txt"


def read_grid(f: str):
    grid = []
    with open(f, "r") as f:
        for line in f:
            grid.append([c for c in line.strip()])
    return grid


def is_roll_at(grid: list[list[str]], i: int, j: int):
    r, c = len(grid), len(grid[0])

    if not 0 <= i < r or not 0 <= j < c:
        return False

    return grid[i][j] == "@"


def get_accessible_rolls(grid: list[list[str]]) -> list[tuple[int, int]]:
    indices = []
    r, c = len(grid), len(grid[0])

    for i in range(r):
        for j in range(c):
            if grid[i][j] != "@":
                continue

            coords = set(
                [(i + dy, j + dx) for dy in range(-1, 2) for dx in range(-1, 2)]
            ) - {(i, j)}

            neighbor_rolls = sum(
                [is_roll_at(grid, coord[0], coord[1]) for coord in coords]
            )

            if neighbor_rolls < 4:
                indices.append((i, j))

    return indices


def get_total_rolls_removed(grid: list[list[str]]):
    rolls = 0

    while True:
        indices = get_accessible_rolls(grid)
        rolls += len(indices)

        # can't remove anymore rolls
        if len(indices) == 0:
            break

        for i, j in indices:
            grid[i][j] = "."

    return rolls


grid = read_grid(input_file)
rolls = get_total_rolls_removed(grid)

print("rolls: ", rolls)
