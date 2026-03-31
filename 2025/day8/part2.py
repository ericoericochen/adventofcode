# input_file = "./inputs/test.txt"
input_file = "./inputs/day8.txt"


def read_junction_boxes(fp: str):
    boxes = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            coords = [int(n) for n in line.split(",")]
            boxes.append(coords)

    return boxes


def straight_line_distance(a: list[int], b: list[int]):
    distance = 0
    for v1, v2 in zip(a, b):
        distance += (v1 - v2) ** 2
    return distance**0.5


def compute_product(l: list):
    product = 1
    for v in l:
        product *= v
    return product


def main(boxes: list[list[int]]):
    N = len(boxes)
    distances = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        a = boxes[i]
        for j in range(N):
            b = boxes[j]
            distance = straight_line_distance(a, b)
            distances[i][j] = distance

    # (i, j), distance between b_i and b_j
    pairwise_distances = []
    for i in range(N):
        for j in range(N):
            if i < j:
                distance = distances[i][j]
                pairwise_distances.append(((i, j), distance))

    entire_circuit = set(range(N))
    asc_pairwise_distances = sorted(pairwise_distances, key=lambda d: d[1])
    boxes_to_circuits: dict[int, set[int]] = {}

    for (i, j), distance in asc_pairwise_distances:
        ic = boxes_to_circuits.get(i, None)
        jc = boxes_to_circuits.get(j, None)

        # new circuit if i and j both don't belong to an existing circuit
        if ic is None and jc is None:
            circuit = set([i, j])
            boxes_to_circuits[i] = circuit
            boxes_to_circuits[j] = circuit
        elif ic is not None and jc is not None:
            circuit = ic | jc
            for n in circuit:
                boxes_to_circuits[n] = circuit
        # add j to circuit i is in
        elif ic is not None:
            ic.add(j)
            boxes_to_circuits[j] = ic
            circuit = ic
        # add i to circuit j is in
        elif jc is not None:
            jc.add(i)
            boxes_to_circuits[i] = jc
            circuit = jc

        if circuit == entire_circuit:
            a = boxes[i]
            b = boxes[j]
            return a[0] * b[0]


boxes = read_junction_boxes(input_file)
result = main(boxes)
print("result: ", result)
