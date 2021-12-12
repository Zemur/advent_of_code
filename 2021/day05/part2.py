def build_vent(coordinates):
    start, end = [i.split(',') for i in coordinates]
    start = list(map(int, [i for i in start]))
    end = list(map(int, [i for i in end]))
    vent = []

    if start[0] == end[0]:
        if end[1] < start[1]:
            start, end = end, start
        for i in range(start[1], end[1]):
            vent.append([start[0], i])
    elif start[1] == end[1]:
        if end[0] < start[0]:
            start, end = end, start
        for i in range(start[0], end[0]):
            vent.append([i, start[1]])
    else:
        slope = (end[1] - start[1]) / (end[0] - start[0])
        if start[0] > end[0]:
            start, end = end, start
        x = start[0]
        y = start[1]
        while x != end[0] and y != end[1]:
            vent.append([x, y])
            x += 1
            if slope < 0:
                y -= 1
            else:
                y += 1
    vent.append(end)
    return vent


def pretty_print_grid(grid_to_print):
    print('='*20)
    for r in grid_to_print:
        print(''.join([str(i) for i in r]))
    print('='*20)


def mark_grid(vent, grid):
    if len(vent) <= 1:
        return grid
    for coords in vent:
        x, y = coords
        if grid[y][x] == '.':
            grid[y][x] = 1
        else:
            grid[y][x] += 1

    return grid


if __name__ == '__main__':
    vents = []
    max_x = 0
    max_y = 0
    with open('input', 'r') as f:
        while i := f.readline():
            coords = [j for j in i.strip().split(' -> ')]
            for coord in coords:
                x, y = list(map(int, coord.split(',')))
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y
            vents.append(build_vent(coords))

    # Initialize grid
    grid = []
    for i in range(max_y+1):
        grid.append(['.']*(max_x+1))

    for vent in vents:
        grid = mark_grid(vent, grid)

    # Get overlaps
    overlaps = 0
    for row in grid:
        for col in row:
            if isinstance(col, int) and col > 1:
                overlaps += 1

    pretty_print_grid(grid)
    print('Overlaps:', overlaps)
