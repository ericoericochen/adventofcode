input_file = "./inputs/day7.txt"


def read_manifold(fp: str):
    splitter_locs = []
    r, c = 0, 0
    start_loc = None
    with open(fp, "r") as f:
        y = 0
        for line in f:
            line = line.strip()
            c = len(line)
            r += 1

            for x, node in enumerate(line):
                if node == "S":
                    start_loc = (y, x)
                elif node == "^":
                    splitter_locs.append((y, x))

            y += 1

    return {"start_loc": start_loc, "splitter_locs": splitter_locs, "r": r, "c": c}


def count_timelines(manifold):
    start_loc = manifold["start_loc"]
    splitter_locs = set(manifold["splitter_locs"])
    r, c = manifold["r"], manifold["c"]

    f = [[0 for j in range(c)] for i in range(r)]

    for i in range(c):
        f[r - 1][i] = 1

    for j in range(r - 2, -1, -1):
        for i in range(c):
            if (j, i) in splitter_locs:
                f[j][i] = f[j + 1][i - 1] + f[j + 1][i + 1]
            else:
                f[j][i] = f[j + 1][i]

    return f[0][start_loc[1]]


manifold = read_manifold(input_file)
timelines = count_timelines(manifold)

print("timelines: ", timelines)
