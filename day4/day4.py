#https://adventofcode.com/2025/day/4

def day4(part2 : bool):
    with open('input.txt') as f:
        grid = [list(r) for r in f.read().splitlines()]
        return removable_for_grid(grid, 0, part2)

# In the part 2 iterate until rolls can be removed.
def removable_for_grid(grid : list, acc : int, part2 : bool) -> int:
    removable = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if can_be_accessed(grid, i, j):
                removable += 1
                if part2:
                    grid[i][j] = '.'

    if not part2:
        return removable

    if removable == 0:
        return acc

    return removable_for_grid(grid, acc + removable, part2)

def can_be_accessed(grid : list, i : int, j : int) -> bool:
    count = 0
    r = len(grid)
    c = len(grid[0])
    # Just to avoid nested loop later.
    dir = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1], [-1, 1], [1, -1]]

    if grid[i][j] == '.':
        return False
    for d in dir:
        if (0 <= i + d[0] < r and 0 <= j + d[1] < c and grid[i+d[0]][j+d[1]] == '@'):
            count += 1
            if count >= 4:
                return False
    
    return True

if __name__ == '__main__':
    print(day4(False))
    print(day4(True))