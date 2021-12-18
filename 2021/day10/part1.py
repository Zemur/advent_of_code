def calc_score(illegal_characters):
    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score_sum = 0
    for i in illegal_chars:
        score_sum += score_table[i]

    return score_sum


def check_line(line):
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    close_map = {cl: op for op, cl in zip(open_tup, close_tup)}
    queue = []

    for i in line:
        if i in open_tup:
            queue.append(i)
        elif i in close_tup:
            j = queue.pop()
            if close_map[i] != j:
                return i


if __name__ == '__main__':
    illegal_chars = []

    with open('input', 'r') as f:
        chunks = [i.strip() for i in f.readlines()]

    for chunk_line in chunks:
        check = check_line(chunk_line)
        if check:
            illegal_chars.append(check)

    print(calc_score(illegal_chars))
