input_file = "./inputs/day6.txt"
# input_file = "./inputs/test.txt"


def read_problem(fp: str):
    with open(fp, "r") as f:
        lines = [line for line in f]
        problem = []

        last_line = lines[-1]
        operators = [last_line[0]]
        digits = []
        current_digits = 0

        for i in range(1, len(last_line)):
            if last_line[i] == " ":
                current_digits += 1
            else:
                operators.append(last_line[i])
                digits.append(current_digits)
                current_digits = 0

        digits.append(current_digits + 1)

        for i in range(len(lines) - 1):
            numbers = []
            line = lines[i].strip("\n")

            prev = 0
            for d in digits:
                numbers.append(line[prev : prev + d])
                prev += d + 1

            problem.append(numbers)
        problem.append(operators)
        return problem, digits


def get_numbers(problem: list[list], digits: list[int], c: int):
    r = len(problem)
    d = digits[c]
    ns = [problem[i][c] for i in range(r - 1)]
    numbers = []

    for i in range(d):
        n = ""
        for j in range(r - 1):
            n += ns[j][i]
        numbers.append(int(n))
    return numbers


def compute_product(ns: list):
    product = 1
    for n in ns:
        product *= n
    return product


def solve_problem(problem: list[list], digits: list[int]) -> int:
    solution = 0
    r, c = len(problem), len(problem[0])

    for i in range(c):
        operator = problem[r - 1][i]
        numbers = get_numbers(problem, digits, i)

        if operator == "+":
            solution += sum(numbers)
        elif operator == "*":
            solution += compute_product(numbers)

    return solution


problem, digits = read_problem(input_file)
solution = solve_problem(problem, digits)
print("solution: ", solution)
