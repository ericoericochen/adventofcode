input_file = "./inputs/day6.txt"


def read_problem(fp: str):
    with open(fp, "r") as f:
        lines = [line for line in f]
        problem = []
        for i in range(len(lines)):
            line = lines[i]
            if i == len(lines) - 1:
                operators = line.strip().split()
                problem.append(operators)
                break

            numbers = [int(n) for n in line.strip().split()]
            problem.append(numbers)
        return problem


def solve_problem(problem: list[list]) -> int:
    solution = 0
    r, c = len(problem), len(problem[0])

    for i in range(c):
        operator = problem[r - 1][i]
        if operator == "+":
            result = sum([problem[k][i] for k in range(r - 1)])
            solution += result
        elif operator == "*":
            product = 1
            for k in range(r - 1):
                product *= problem[k][i]
            solution += product

    return solution


problem = read_problem(input_file)
solution = solve_problem(problem)
print("solution: ", solution)
