import heapq

# input_file = "./inputs/test2.txt"
input_file = "./inputs/day10.txt"


def read_problems(fp: str):
    problems = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            els = line.split(" ")
            goal = els[0]
            buttons = els[1:-1]
            joltage = els[-1]

            goal = tuple([s for s in goal[1:-1]])
            buttons = [tuple(map(int, btn[1:-1].split(","))) for btn in buttons]
            joltage = tuple(map(int, joltage[1:-1].split(",")))
            problems.append((goal, buttons, joltage))
    return problems


def update_counter(counter, button, n: int = 1):
    updated_counter = []

    for i, c in enumerate(counter):
        if i in button:
            c += n
        updated_counter.append(c)
    return tuple(updated_counter)


def get_max_updates(counter, goal, button):
    cs = [counter[i] for i in button]
    gs = [goal[i] for i in button]
    max_updates = float("inf")
    for g, c in zip(gs, cs):
        max_updates = min(max_updates, g - c)
    return max_updates


def should_prune(counter, goal):
    for c, g in zip(counter, goal):
        if c > g:
            return True
    return False


def h(counter, goal):
    r = 0
    for g, c in zip(goal, counter):
        r = max(r, g - c)
    return r


# def h(counter, goal):
#     r = 0
#     for g, c in zip(goal, counter):
#         r += g - c
#     return r


# def h(counter, goal):
#     return 0


# heuristic
def compute_cost(node, goal):
    counter, presses = node
    # actual cost + heuristic
    return presses + h(counter, goal)


# use A-star
# use prunning - prun nodes that can never reach the goal joltage
def get_fewest_button_presses(problem):
    _, buttons, joltage = problem
    start = (0,) * len(joltage)

    # priority queue
    queue = []
    start_node = (start, 0)
    start_cost = compute_cost(start_node, joltage)
    heapq.heappush(queue, (start_cost, start_node))
    best_presses = {start: 0}

    while queue:
        node_with_cost = heapq.heappop(queue)
        cost, node = node_with_cost
        counter, presses = node

        if counter == joltage:
            return presses

        for button in buttons:
            # max_updates = get_max_updates(counter, joltage, button)
            # for updates in range(1, max_updates + 1):
            for updates in range(1, 2):
                next_counter = update_counter(counter, button, n=updates)
                new_presses = presses + updates
                if new_presses < best_presses.get(next_counter, float("inf")):
                    best_presses[next_counter] = new_presses
                    next_node = (next_counter, new_presses)
                    next_cost = compute_cost(next_node, joltage)
                    print(next_counter, joltage)
                    heapq.heappush(queue, (next_cost, next_node))

    # print("didn't find a solution")


def main(problems):
    result = 0
    for problem in problems:
        result += get_fewest_button_presses(problem)
        print("found solution")
    return result


problems = read_problems(input_file)

import time

start = time.perf_counter()
result = main(problems[:1])
duration = time.perf_counter() - start
print(duration)
print("result: ", result)
