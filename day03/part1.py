def solve(filename):
    result = 0
    with open(filename, 'r', encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            result += get_max_value(line)

    return result


def get_max_value(line):
    left_max = -1
    right_max = -1

    for index, c in enumerate(line):
        num = int(c)
        if num > left_max and index != len(line) - 1:
            left_max = num
            right_max = -1
        elif num > right_max:
            right_max = num

    return left_max * 10 + right_max


if __name__ == "__main__":
    solved_result = solve('./input-test.txt')
    print(f"Test result {solved_result}")

    solved_result = solve('./input-full.txt')
    print(f"Full result {solved_result}")
