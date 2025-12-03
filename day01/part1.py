def solve(filename):
    result = 0
    position = 50
    with open(filename, 'r', encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            number = int(line[1:])
            if direction == 'L':
                position -= number
            else:
                position += number

            position = position % 100
            if position == 0:
                result += 1

    return result


if __name__ == "__main__":
    solved_result = solve('./input-test.txt')
    print(f"Test result {solved_result}")

    solved_result = solve('./input-full.txt')
    print(f"Full result {solved_result}")
