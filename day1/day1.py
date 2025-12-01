# https://adventofcode.com/2025/day/1

def day1_p1():
    with open("input.txt") as f:
        doc = f.read()
        rotations = doc.split('\n')
        current = 50
        res = 0

        for r in rotations:
            direction = r[0]
            distance = int(r[1:])
            if direction == 'R':
                current = (current + distance) % 100
            else:
                current = (current - distance) % 100

            if current == 0:
                res += 1

    print(res)

def day1_p2():
    with open("input.txt") as f:
        doc = f.read()
        rotations = doc.split('\n')
        current = 50
        res = 0

        for r in rotations:
            direction = r[0]
            distance = int(r[1:])

            # How many times passes 0
            turns = distance // 100
            res += turns

            # What is left?
            left = distance % 100

            # Go one by one
            for __ in range(left):
                if direction == 'R':
                    current = (current + 1) % 100
                else:
                    current = (current - 1) % 100

                if current == 0:
                    res += 1

    print(res)

if __name__ == '__main__':
    day1_p1()
    day1_p2()