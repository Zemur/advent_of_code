import sys
from octopus import Octopus


def pretty_print_matrix(matrix):
    return '\n'.join([''.join([str(octopus.energy) for octopus in r]) for r in matrix])


def synchronized_flash(matrix):
    return sum(([i.energy for i in sum(matrix, [])])) == 0


if __name__ == '__main__':
    with open('input', 'r') as f:
        octopi = [list(i.strip()) for i in f.readlines()]
        for i, row in enumerate(octopi):
            for j, col in enumerate(row):
                octopi[i][j] = Octopus(int(octopi[i][j]))

    step = 0
    flash_total = 0

    while not synchronized_flash(octopi):
        for y, row in enumerate(octopi):
            for x, col in enumerate(row):
                col.increase()
        flash = True
        while flash:
            flash = False
            for y, row in enumerate(octopi):
                for x, col in enumerate(row):
                    if col.flashed == 1:
                        col.flash()
                        flash_total += 1
                        flash = True
                        possible_adjacent_cells = [(x - 1, y),  # left
                                                   (x + 1, y),  # right
                                                   (x, y - 1),  # up
                                                   (x, y + 1),  # down
                                                   (x + 1, y - 1),  # right up
                                                   (x + 1, y + 1),  # right down
                                                   (x - 1, y - 1),  # left up
                                                   (x - 1, y + 1)]  # left down
                        real_adjacent = [(x, y) for x, y in possible_adjacent_cells
                                         if 0 <= x < len(row) and 0 <= y < len(octopi)]
                        for ax, ay in real_adjacent:
                            octopi[ay][ax].increase()

        count = 0
        for y, row in enumerate(octopi):
            for x, col in enumerate(row):
                col.reset()
        print(f"After step {step + 1}")
        print(pretty_print_matrix(octopi))
        step += 1
        print('---')

    print(f"Number of flashes: {flash_total}")
    print(f"Synchronized on step: {step}")
