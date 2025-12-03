def solve(filename):
    result = 0
    position = 50
    with open(filename, 'r', encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            number = int(line[1:])
            previous_position = position
            if direction == 'L':
                position -= number
            else:
                position += number

            result += calculate_zero_position(position, previous_position)
            position = position % 100

    return result


def calculate_zero_position(position, previous_position):
    if position == 0:
        return 1

    if position < 0:
        negative = 0 if previous_position == 0 else 1
        return negative + int(-position / 100)

    return position // 100


if __name__ == "__main__":
    solved_result = solve('./input-test.txt')
    print(f"Test result {solved_result}")

    solved_result = solve('./input-full.txt')
    print(f"Full result {solved_result}")
