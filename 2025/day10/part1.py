input_file = "./inputs/test2.txt"
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
            joltage = list(map(int, joltage[1:-1].split(",")))
            problems.append((goal, buttons, joltage))
    return problems


def toggle_state(state):
    if state == ".":
        return "#"
    else:
        return "."


def toggle(machine, button):
    state = []
    for i, s in enumerate(machine):
        if i in button:
            s = toggle_state(s)
        state.append(s)

    return tuple(state)


def get_fewest_button_presses(problem):
    goal, buttons, joltage = problem
    start = (".",) * len(goal)

    # each node contains the machine indicator lights and the number of button presses to get there
    # initialize start node with 0 button presses
    queue = [(start, 0)]
    visited = set([start])

    while queue:
        node = queue.pop(0)
        state, presses = node

        if state == goal:
            return presses

        for button in buttons:
            next_state = toggle(state, button)
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, presses + 1))


def main(problems):
    result = 0
    for problem in problems:
        result += get_fewest_button_presses(problem)
    return result


problems = read_problems(input_file)
result = main(problems)
print("result: ", result)
