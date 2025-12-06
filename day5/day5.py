# https://adventofcode.com/2025/day/5

def day5_p1():
    with open('input.txt') as f:
        database = f.read()
        tables = database.split('\n\n')
        
        ranges = tables[0].splitlines()
        ranges = [rg.split('-') for rg in ranges]
        ids = tables[1].splitlines()

        fresh = 0

        for id in ids:
            for rg in ranges:
                if int(rg[0]) <= int(id) <= int(rg[1]):
                    fresh += 1
                    break
        return fresh


def day5_p2():
    with open('input.txt') as f:
        database = f.read()
        tables = database.split('\n\n')
        
        # The idea is to make an union of all the ranges without overlapping.
        ranges = tables[0].splitlines()
        ranges = [tuple(rg.split('-')) for rg in ranges]
        ranges = [(int(x), int(y)) for (x, y) in ranges]
        ranges = sorted(ranges)

        fresh = 0
        cursor = -1

        for lower, upper in ranges:
            # Current range starts behind the current max.
            if cursor >= lower:
                lower = cursor + 1
            # Moving range, needs validation.
            if lower <= upper:
                fresh += upper - lower + 1
            # Move the cursor to the end of the ranges union
            cursor = max(cursor, upper)

        return fresh

if __name__ == '__main__':
    print(day5_p1())
    print(day5_p2())