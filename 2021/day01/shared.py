def read_input():
    with open('input') as f:
        return list(map(int, map(str.strip, f.readlines())))


def compare_depth(depth_readings):
    num_increases = 0

    for i in range(len(depth_readings)):
        if i == 0:
            print(depth_readings[i], "(N/A - no previous measurement)")
        elif depth_readings[i-1] == depth_readings[i]:
            print(depth_readings[i], "(no change)")
        elif depth_readings[i - 1] < depth_readings[i]:
            print(depth_readings[i], "(increased)")
            num_increases += 1
        else:
            print(depth_readings[i], "(decreased)")

    return num_increases
