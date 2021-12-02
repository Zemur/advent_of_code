if __name__ == '__main__':
    horizontal_pos = 0
    depth = 0
    aim = 0

    with open('input', 'r') as f:
        course_input = [[int(i) if i.isdigit() else i for i in i.strip().split(' ')] for i in f.readlines()]

    for input_direction, input_unit in course_input:
        if input_direction == 'forward':
            horizontal_pos += input_unit
            depth += aim * input_unit
        elif input_direction == 'down':
            aim += input_unit
        elif input_direction == 'up':
            aim -= input_unit

    print(depth * horizontal_pos)
