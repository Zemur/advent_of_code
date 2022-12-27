def find_overlap(cleaning_pair):
    expanded_pairs = []
    for assignment in cleaning_pair:
        start, end = map(int, assignment.split('-'))
        expanded_pairs.append([i for i in range(start, end + 1)])

    return (
            any(i in expanded_pairs[0] for i in expanded_pairs[1]) or
            any(i in expanded_pairs[1] for i in expanded_pairs[0])
    )


if __name__ == '__main__':
    with open('input') as f:
        contained_pairs = 0
        for i in [i.strip().split(',') for i in f.readlines()]:
            if find_overlap(i):
                contained_pairs += 1

    print(contained_pairs)
