def find_low_points(height_map):
    low_points = []
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
                low_points.append(height_map[i][j])

    return low_points


if __name__ == '__main__':
    with open('input', 'r') as f:
        lava_map = [list(i.strip()) for i in f.readlines()]

    risk_levels = [int(i)+1 for i in find_low_points(lava_map)]
    print(sum(risk_levels))
