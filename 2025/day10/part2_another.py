import heapq

input_file = "./inputs/test2.txt"
# input_file = "./inputs/day10.txt"


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


def press_button(action_counts, button_idx):
    next_counts = list(action_counts)
    next_counts[button_idx] += 1
    return tuple(next_counts)


def compute_counter(action_counts, buttons, num_lights):
    counter = [0] * num_lights
    for button_idx, presses in enumerate(action_counts):
        if presses == 0:
            continue
        for light_idx in buttons[button_idx]:
            counter[light_idx] += presses
    return tuple(counter)


def should_prune(counter, goal):
    for c, g in zip(counter, goal):
        if c > g:
            return True
    return False


def reached_goal(actions, goal, buttons, joltage):
    pass


# use A-star
# use prunning - prun nodes that can never reach the goal joltage
def get_fewest_button_presses(problem):
    _, buttons, joltage = problem
    start = (0,) * len(buttons)

    # priority queue
    queue = [(start, 0)]
    visited = set([start])

    while queue:
        _, action_counts, counter = heapq.heappop(queue)
        presses = sum(action_counts)

        if presses > best_presses.get(action_counts, float("inf")):
            continue

        if counter == joltage:
            return presses

        for button_idx in range(len(buttons)):
            next_action_counts = press_button(action_counts, button_idx)
            next_counter = compute_counter(next_action_counts, buttons, len(joltage))
            if should_prune(next_counter, joltage):
                continue

            next_presses = presses + 1
            if next_presses < best_presses.get(next_action_counts, float("inf")):
                best_presses[next_action_counts] = next_presses
                next_cost = compute_cost(next_action_counts, next_counter, joltage)
                heapq.heappush(queue, (next_cost, next_action_counts, next_counter))

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
