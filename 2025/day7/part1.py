input_file = "./inputs/day7.txt"
# input_file = "./inputs/test.txt"


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


def count_beam_splits(manifold):
    start_loc = manifold["start_loc"]
    splitter_locs = set(manifold["splitter_locs"])
    r, c = manifold["r"], manifold["c"]

    # bfs
    queue = [start_loc]
    visited = set()
    visited_splitter_locs = set()

    while queue:
        node = queue.pop(0)
        y, x = node

        # reached bottom of manifold
        if y == r - 1:
            continue

        if node in splitter_locs:
            visited_splitter_locs.add(node)
            next_nodes = [(y + 1, x - 1), (y + 1, x + 1)]
        else:
            next_nodes = [(y + 1, x)]

        for next_node in next_nodes:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

    return len(visited_splitter_locs)


manifold = read_manifold(input_file)
beam_splits = count_beam_splits(manifold)

print("beam_splits: ", beam_splits)
