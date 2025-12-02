# https://adventofcode.com/2025/day/2

def day2(part2 : bool):
    with open('input.txt') as f:
        ranges = f.read().split(',')
        res = 0

        for r in ranges:
            rg = r.split('-')
            lower = int(rg[0])
            upper = int(rg[1])

            for id in range(lower, upper + 1):
                if (is_invalid_id(id, part2)):
                    res += id

    return res

def is_invalid_id(id: int, part2 : bool) -> bool:
    s = str(id)
    m = len(s) // 2
    if (part2):
        # Sequence of digits repeated at least twice
        # 565656
        while m >= 1:
            parts = [s[i:i+m] for i in range(0, len(s), m)]
            if len(set(parts)) == 1:
                return True
            m -= 1
        return False
    else:
        # Sequence of digits repeated twice
        # 1188511885
        # 999
        return s[:m] == s[m:]


if __name__ == '__main__':
    print(day2(False))
    print(day2(True))