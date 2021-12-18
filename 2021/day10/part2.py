import sys


def calc_autocomplete_score(autocompletes):
    score_table = {ch: score for ch, score in zip(list(')]}>'), range(1, 5))}
    score = 0

    for char in autocompletes:
        score *= 5
        score += score_table[char]

    return score


def calc_illegal_score(illegal_characters):
    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score_sum = 0
    for i in illegal_characters:
        score_sum += score_table[i]

    return score_sum


def check_for_corrupted(line):
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    close_map = {cl: op for op, cl in zip(open_tup, close_tup)}
    # open_map = {op: cl for op, cl in zip(open_tup, close_tup)}
    queue = []

    for i in line:
        if i in open_tup:
            queue.append(i)
        elif i in close_tup:
            j = queue.pop()
            if close_map[i] != j:
                # Corrupted
                # print(f"Expected {open_map[j]}, but found {i} instead.")
                return [i, 'Corrupted']

    return [None, None]


def autocomplete(line):
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    open_map = {op: cl for op, cl in zip(open_tup, close_tup)}
    queue = []
    closing_chars = []

    for i in line:
        if i in open_tup:
            queue.append(i)
        if i in close_tup:
            queue.pop()

    for unbalanced_open in queue[::-1]:
        closing_chars.append(open_map[unbalanced_open])

    return closing_chars


if __name__ == '__main__':
    illegal_chars = []
    uncorrupted_lines = []
    autocompletes = []
    ac_scores = []

    with open('input', 'r') as f:
        chunks = [i.strip() for i in f.readlines()]

    for chunk_line in chunks:
        check, state = check_for_corrupted(chunk_line)
        if state == 'Corrupted':
            illegal_chars.append(check)
        else:
            uncorrupted_lines.append(chunk_line)

    print(calc_illegal_score(illegal_chars))

    autocompletes = [autocomplete(i) for i in uncorrupted_lines]
    ac_scores = [calc_autocomplete_score(i) for i in autocompletes]

    print(sorted(ac_scores)[len(ac_scores) // 2])
