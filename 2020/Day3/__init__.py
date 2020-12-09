import math


def traverse(map_file, move_x, move_y):
    x_pos = 0
    y_pos = 0
    tree_count = 0
    with open(map_file) as f:
        tree_map = [x.strip() for x in f.readlines()]

    for i in tree_map:
        x_pos += move_x
        y_pos += move_y

        if y_pos >= len(tree_map):
            break
        if x_pos >= len(i):
            x_pos = x_pos - len(i)
        if tree_map[y_pos][x_pos] == '#':
            tree_count += 1
    return tree_count


if __name__ == '__main__':
    slopes = [traverse('input', 1, 1),
              traverse('input', 3, 1),
              traverse('input', 5, 1),
              traverse('input', 7, 1),
              traverse('input', 1, 2)]

    print(math.prod(slopes))
