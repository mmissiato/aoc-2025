# https://adventofcode.com/2025/day/7

def day7_p1():
    with open('input.txt') as f:
        lines = [line for line in f.read().splitlines()]

    d = {}
    r = len(lines)
    c = len(lines[0])
    start = (0, lines[0].index('S'))

    d[start[1]] = 1
    split_count = 0

    for i in range(2, r, 2):
        line = lines[i]
        for j, s in enumerate(line):
            v = d.get(j)
            if v :
                if s == '^':
                    split_count += 1
                    del d[j]
                    if i+1 < r and j+1 < c:
                        d[j+1] = i+1
                        d[j-1] = i+1
    return split_count


def count_timelines(grid, i, j, mem):
    r = len(grid)
    c = len(grid[0])

    if (i, j) in mem:
        return mem[(i, j)]

    if i >= r or j < 0 or j >= c:
        return 1
        
    c = grid[i][j]
    
    if c == '^':
        left = count_timelines(grid, i+1, j-1, mem)
        right = count_timelines(grid, i+1, j+1, mem)
        t = left + right
        mem[(i, j)] = t
        return t

    return count_timelines(grid, i+1, j, mem)

def day7_p2():
    with open('input.txt') as f:
        lines = [line for line in f.read().splitlines()]

    grid = [list(line) for line in lines]
    start_col = grid[0].index('S')
    
    mem = {}
    return count_timelines(grid, 1, start_col, mem)

if __name__ == '__main__':
    print(day7_p1())
    print(day7_p2())