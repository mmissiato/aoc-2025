# https://adventofcode.com/2025/day/6
from functools import reduce

def day6_p1():
    with open('input.txt') as f:
        lines = [line.split() for line in f]

    # Transpose
    grid = list(zip(*lines))

    grand_total = 0

    for problem in grid:
        *numbers, op = problem
        numbers = map(int, numbers)

        if op == '*':
            total = reduce(lambda acc, num: acc * num, numbers, 1)
        else:
            total = sum(numbers)

        grand_total += total

    return grand_total

def day6_p2():
    with open('input.txt') as f:
        lines = f.read().split('\n')

    grid = [list(row) for row in lines]

    grand_total = 0
    ops_line = grid[-1]

    # Get all operator positions.
    # Ops with start and end which give the "column" width.
    op_positions = [(i, c) for i, c in enumerate(ops_line) if c in "+*"]
    segments = []
    for idx, (pos, op) in enumerate(op_positions):
        start = pos

        # End is right before the next operator, otherwise end at line end.
        if idx + 1 < len(op_positions):
            end = op_positions[idx + 1][0] - 1
        else:
            end = len(ops_line) - 1

        segments.append((op, start, end))


    for op, start, end in segments:
        total = 1 if op == '*' else 0
        for i in range(start-1, end):
            num = ''
            for j in range(len(grid)-1):
                row = grid[j]
                c = row[i]
                if c != ' ':
                    num += c
            if num != '':
                num = int(num)
                if op == "*":
                    total *= num
                else:
                    total += num
        grand_total += total
    return grand_total


if __name__ == '__main__':
    print(day6_p1())
    print(day6_p2())