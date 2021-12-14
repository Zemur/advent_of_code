from collections import deque
import math


def adjacent(height_map, x, y):
    possible_adjacent = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(i, j) for (i, j) in possible_adjacent if 0 <= i < len(height_map) and 0 <= j < len(height_map[0])]


def find_basin(height_map, coordinates):
    basin = []
    visited = set()
    queue = deque([(coordinates[0], coordinates[1])])

    while queue:
        (curr_x, curr_y) = queue.pop()
        if (curr_x, curr_y) in visited:
            continue
        else:
            visited.add((curr_x, curr_y))
            if int(height_map[curr_x][curr_y]) != 9:
                basin.append((curr_x, curr_y))
                queue.extend([(i, j) for (i, j) in adjacent(height_map, curr_x, curr_y) if (i, j) not in visited])
    return basin


def find_low_points(height_map):
    lows = []
    for i, row in enumerate(height_map):
        for j, col in enumerate(row):
            curr_location = height_map[i][j]
            lower_locations = []
            # right
            if j + 1 < len(row):
                lower_locations.append(curr_location < height_map[i][j+1])
            # left
            if j - 1 >= 0:
                lower_locations.append(curr_location < height_map[i][j-1])
            # up
            if i - 1 >= 0:
                lower_locations.append(curr_location < height_map[i-1][j])
            # down
            if i + 1 < len(height_map):
                lower_locations.append(curr_location < height_map[i+1][j])
            if all(lower_locations):
                lows.append([i, j])
    return lows


if __name__ == '__main__':
    basin_sizes = []
    with open('input', 'r') as f:
        lava_map = [list(i.strip()) for i in f.readlines()]

    low_points = find_low_points(lava_map)
    for lp in low_points:
        basin_sizes.append(len(find_basin(lava_map, lp)))

    print(math.prod(sorted(basin_sizes)[-3:]))
