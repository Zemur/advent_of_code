import re

if __name__ == '__main__':
    stack_layout = []
    instructions = []
    with open('input') as f:
        for line in f:
            if line.startswith('[') or line.startswith(' ') and not line.startswith(' 1'):
                # Brute force for the longest line.
                # This can be improved to be dynamic.
                if len(line) < 35:
                    line = line.rstrip("\n") + "    \n"
                stack_layout.append(list(map(str.strip, re.findall(r'...\s', line))))
            elif line.startswith('move'):
                instructions.append(re.findall('\d+', line.strip()))
    rotated_stack = [list(i) for i in zip(*stack_layout[::-1])]

    for i, row in enumerate(rotated_stack):
        rotated_stack[i] = [j for j in row if j != '']

    for instruction in instructions:
        num_move = int(instruction[0])
        from_stack = int(instruction[1]) - 1
        to_stack = int(instruction[2]) - 1
        for _ in range(num_move):
            rotated_stack[to_stack].append(rotated_stack[from_stack].pop())
    print(''.join(re.findall(r'\w+', ''.join([i[-1] for i in rotated_stack]))))
