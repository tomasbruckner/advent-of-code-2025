def solve(filename):
    result = 0
    with open(filename, 'r', encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            result += get_max_value(line)

    return result


def get_max_value(line):
    max_nums = [0] * 12

    for c_index, c in enumerate(line):
        num = int(c)

        rest_in_line = len(line) - c_index
        for n_index, n in enumerate(max_nums):
            rest_in_max = 12 - n_index
            if n < num and rest_in_line >= rest_in_max:
                max_nums[n_index] = num
                for j in range(n_index + 1, 12):
                    max_nums[j] = 0

                break

    result = ''.join(str(n) for n in max_nums)

    return int(result)


if __name__ == "__main__":
    solved_result = solve('./input-test.txt')
    print(f"Test result {solved_result}")

    solved_result = solve('./input-full.txt')
    print(f"Full result {solved_result}")
