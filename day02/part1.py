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
        num_str = str(num)
        mid = len(num_str) // 2
        first = num_str[:mid]
        second = num_str[mid:]
        if first == second:
            result += num

    return result


if __name__ == "__main__":
    solved_result = solve('./input-test.txt')
    print(f"Test result {solved_result}")

    solved_result = solve('./input-full.txt')
    print(f"Full result {solved_result}")
