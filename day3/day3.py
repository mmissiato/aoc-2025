# https://adventofcode.com/2025/day/3

# DP
def evaluate_bank(bank : list[int], i : int, consumed : int, n : int, cache : dict) -> int:
    # End of the bank with the required digits
    if i == len(bank) and consumed == n:
        return 0
    # End of the bank but not enough required digits -> discard
    if i == len(bank):
        return float('-inf')
    k = (i, consumed)
    if k in cache:
        return cache[k]
    voltage = evaluate_bank(bank, i+1, consumed, n, cache)
    if consumed < n:
        voltage = max(voltage, 10 ** (n-consumed-1) * int(bank[i])
                + evaluate_bank(bank, i+1, consumed+1, n, cache))

    cache[k] = voltage
    return voltage

# Greedy
def evaluate_bank_1(bank : list[int], i : int, n : int, acc : str) -> str:
    if i == len(bank) or len(acc) == n:
        return acc

    # Look for the max considering how many we still need.
    remaining = n - len(acc)
    end = len(bank) - remaining
    valid_range = bank[i:end+1]
    mx = max(valid_range)
    index = valid_range.index(mx) + i

    return evaluate_bank_1(bank, index + 1, n, acc + mx)

def day3(part2 : bool, greedy : bool):
    with open('input.txt') as f:
        banks = f.read().split('\n')
        n = 12 if part2 else 2
        sum = 0
        for bank in banks:
            if greedy:
                voltage = int(evaluate_bank_1(bank, 0, n, ''))
            else:
                cache = {}
                voltage = evaluate_bank(bank, 0, 0, n, cache)
            sum += voltage
        
        return sum

if __name__ == '__main__':
    print(day3(False, False))
    print(day3(True, True))