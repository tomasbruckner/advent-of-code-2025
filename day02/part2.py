def solve(filename):
    result = 0
    with open(filename, 'r', encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            pairs = line.split(',')
            for pair in pairs:
                result += get_invalid_value(pair)

    return result


def get_invalid_value(pair):
    result = 0
    (start, end) = pair.split('-')
    start = int(start)
    end = int(end)

    for num in range(start, end + 1):
        if is_invalid(str(num)):
            result += num

    return result


def is_invalid(num_str):
    for i in range(1, len(num_str)):
        pairs = split_by_n(num_str, i)
        if len(set(pairs)) == 1:
            return True

    return False


def split_by_n(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]

if __name__ == "__main__":
    solved_result = solve('./input-test.txt')
    print(f"Test result {solved_result}")

    solved_result = solve('./input-full.txt')
    print(f"Full result {solved_result}")
